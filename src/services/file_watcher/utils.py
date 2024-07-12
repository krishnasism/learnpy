import os
from threading import Thread

from watchdog.observers import Observer

from .file_watcher_event_handler import Handler


def __watch_exercise_files():
    exercises_path = f"{os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(os.path.dirname(os.path.realpath(__file__))))))}/exercises/"  # noqa: E501
    print(f"Watching: {exercises_path}")
    observer = Observer()
    observer.schedule(Handler(), exercises_path, recursive=True)
    try:
        observer.start()
        observer.join()
    except KeyboardInterrupt:
        observer.stop()


async def watch_exercise_files():
    observer_thread = Thread(target=__watch_exercise_files, daemon=True)
    observer_thread.start()
