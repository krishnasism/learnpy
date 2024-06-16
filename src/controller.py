import asyncio
import io
import logging
import sys
from tomllib import load

import pytest

from src.model.exercise import Exercise
from src.services.communication.queue import get_watcher_queue


def load_exercises_info() -> list[Exercise]:
    """
    Loads the exercises information.
    """
    with open("resources/info.toml", "rb") as f:
        exercises_toml = load(f)
    return [Exercise(**exercise) for exercise in exercises_toml["exercises"]]


def get_correct_and_watched_exercises(exercises: list[Exercise]) -> tuple[list[Exercise], list[Exercise]]:
    correct_exercises = []
    watched_exercises = []
    for exercise in exercises:
        if exercise.is_done():
            # check if exercise is correct
            correct = exercise.run().is_success()
            if correct:
                correct_exercises.append(exercise)
                logging.debug(f"{exercise.name} is correct")
                continue
            else:
                logging.debug(f"{exercise.name} is incorrect")
        watched_exercises.append(exercise)
        logging.debug(f"Watching {exercise.name}")
    return correct_exercises, watched_exercises


def get_exercise_info_dict() -> dict:
    """Transform exercise list into dictionary"""
    exercise_info = load_exercises_info()
    exercise_info_dict = dict()
    for exercise in exercise_info:
        exercise_info_dict[exercise.name] = {"path": exercise.path, "hint": exercise.hint}
    return exercise_info_dict


async def watch_queue():
    """Watches for events pushed by file watcher"""
    queue = get_watcher_queue()
    exercise_info = get_exercise_info_dict()
    while True:
        if not queue.empty():
            item: str = queue.get()
            modified_exercise = item.split("_")[-1].replace(".py", "")
            orig_stdout = sys.stdout
            sys.stdout = io.StringIO()
            ret_code = pytest.main(["-x", item.replace("exercises/", "tests/test_")])
            sys.stdout = orig_stdout
            logging.info("Correct!") if ret_code == 0 else logging.info("Not correct!")
            if ret_code != 0:
                logging.info(f"HINT: {exercise_info[modified_exercise]['hint']}")

        await asyncio.sleep(2)
