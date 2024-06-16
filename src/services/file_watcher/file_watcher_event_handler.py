from watchdog.events import FileSystemEventHandler

from src.services.communication.queue import get_watcher_queue


class Handler(FileSystemEventHandler):
    @staticmethod
    def on_any_event(event):
        if event.is_directory:
            return None
        elif event.event_type == "modified":
            get_watcher_queue().put(event.src_path)
