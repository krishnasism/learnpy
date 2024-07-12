import asyncio

import typer

from src.controller import get_correct_and_watched_exercises, watch_queue
from src.model.exercises import Exercises
from src.services.file_watcher.utils import watch_exercise_files

app = typer.Typer()
exercises = Exercises()


@app.command()
def doc():
    print("Documentation::")


@app.command()
def start():
    """Start learning"""
    print("Watching.. go ahead and finish a problem")
    loop = asyncio.new_event_loop()
    loop.create_task(watch_exercise_files(), name="watch_exercise_files")
    loop.create_task(watch_queue(), name="watch_queue")
    try:
        loop.run_forever()
    except KeyboardInterrupt:
        loop.stop()


@app.command()
def watch():
    correct, watched = get_correct_and_watched_exercises(exercises.all())
    print(f"Correct exercises: {[e.name for e in correct]}")
    print(f"Watched exercises: {[e.name for e in watched]}")


@app.command()
def report():
    correct, _ = get_correct_and_watched_exercises(exercises.all())
    print(f"Finished exercises: {[e.name for e in correct]}")


def main():
    app()
