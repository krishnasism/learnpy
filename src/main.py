import asyncio

import typer

from src.services.communication.queue import get_watcher_queue
from src.services.file_watcher.utils import watch_exercise_files

from .runner import Runner

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
            print(f"[Debug] Something changed with {item}")
        await asyncio.sleep(2)


@app.command()
def run(script_path: str = "src/exercises/9999_test.py"):
    """Run the script"""
    typer.echo(f"Running {script_path}")
    runner = Runner(script_path)
    runner.run()
    typer.echo(runner.get_stdout())


def main():
    app()
