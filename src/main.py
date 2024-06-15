import asyncio
import logging
import os

import typer

from src.controller import watch_queue
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


def main():
    app()
