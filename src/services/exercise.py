from enum import Enum


class Mode(Enum):
    """
    Mode of the exercise.
    An exercise can either be a test or a syntax exercise.
    """

    TEST = "test"
    SYNTAX = "syntax"


class State(Enum):
    """
    State of the exercise.
    An exercise can either be pending or done.
    """

    PENDING = "pending"
    DONE = "done"


class Result:
    """
    Represents the result of running an exercise.
    """


class Exercise:
    """
    Represents an exercise.
    Deserialized from the info.toml file.
    """

    def __init__(self) -> None:
        self.name: str
        self.path: str
        self.mode: Mode
        self.hint: str

    def run(self) -> Result:
        """
        Runs the exercise.
        If the exercise is a test, it runs the test.
        """
        return Result()

    def state(self) -> State:
        """
        Returns the state of the exercise.
        """
        with open(self.path, encoding="UTF-8") as source_code:
            while line := source_code.readline():
                if contains_not_done_comment(line.rstrip()):
                    return State.PENDING
        return State.DONE

    def is_done(self) -> bool:
        """
        Checks if the exercise is done.
        """
        return self.state() == State.DONE


def contains_not_done_comment(line: str) -> bool:
    """
    Checks if the line contains a "# I AM NOT DONE".
    """
    return "# I AM NOT DONE" in line
