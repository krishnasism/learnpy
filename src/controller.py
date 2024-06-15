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


async def watch_queue():
    queue = get_watcher_queue()
    while True:
        if not queue.empty():
            item = queue.get_nowait()
            logging.debug(f"Something changed with {item}")
            orig_stdout = sys.stdout
            sys.stdout = io.StringIO()
            ret_code = pytest.main(["-x", item.replace("exercises/", "tests/test_")])
            sys.stdout = orig_stdout
            logging.info("Correct!") if ret_code == 0 else logging.info("Not correct!")

        await asyncio.sleep(2)
