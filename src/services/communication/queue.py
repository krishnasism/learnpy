import queue

watcher_queue: queue.Queue = queue.Queue()


def get_watcher_queue() -> queue.Queue:
    return watcher_queue
