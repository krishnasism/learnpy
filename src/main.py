import asyncio
import io
import logging
import os
import sys

import pytest
import typer

from src.services.communication.queue import get_watcher_queue
from src.services.file_watcher.utils import watch_exercise_files

DEBUG = os.getenv("LEARNPY_DEBUG", False)
level = logging.DEBUG if DEBUG else logging.INFO
logging.basicConfig(level=level)

app = typer.Typer()


@app.command()
def doc():
    print("Documentation::")


@app.command()
def start():
    """Start learning"""
    loop = asyncio.new_event_loop()
    loop.create_task(watch_exercise_files(), name="watch_exercise_files")
    loop.create_task(watch_queue(), name="watch_queue")
    try:
        loop.run_forever()
    except KeyboardInterrupt:
        loop.stop()


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


def main():
    app()
