import asyncio
import logging
import os

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
def start(debug: bool = False):
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
        await asyncio.sleep(2)


def main():
    app()
