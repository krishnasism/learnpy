import asyncio
import io
import logging
import sys

import aiofiles
import pytest

from src.model.exercise import Exercise
from src.model.exercises import Exercises
from src.services.communication.queue import get_watcher_queue

exercises = Exercises()


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


async def watch_queue():
    """Watches for events pushed by file watcher"""
    queue = get_watcher_queue()
    while True:
        if not queue.empty():
            item: str = queue.get()
            modified_exercise = item.split("_")[-1].replace(".py", "")
            exercise: Exercise = exercises[modified_exercise]
            orig_stdout = sys.stdout
            sys.stdout = io.StringIO()
            if not await is_ready(item):
                logging.info("Don't forget to remove the # I'M NOT DONE when you're done ;)")
                continue
            ret_code = pytest.main(["-x", item.replace("exercises/", "exercise_tests/test_")])
            sys.stdout = orig_stdout
            logging.info("Correct!") if ret_code == 0 else logging.info("Not correct!")
            if ret_code != 0:
                logging.info(f"HINT: {exercise.hint}")

        await asyncio.sleep(2)


async def is_ready(file_path: str) -> bool:
    async with aiofiles.open(file_path) as f:
        contents = await f.read()
    return "# I'M NOT DONE" not in contents
