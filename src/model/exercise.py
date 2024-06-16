import io
import sys
from enum import Enum
from tomllib import load

import pytest


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

    def __init__(self, ret_code: int | pytest.ExitCode) -> None:
        self.ret_code = ret_code

    def is_success(self) -> bool:
        """
        Checks if the result is successful.
        """
        return self.ret_code == 0


class Exercise:
    """
    Represents an exercise.
    """

    def __init__(self, name, path, hint) -> None:
        self.name: str = name
        self.path: str = path
        self.hint: str = hint

    def run(self) -> Result:
        """
        Runs the exercise.
        Each exercise has a corresponding test file which is run to check if the exercise is correct.
        """
        # HACK: This is a hack to disable logging from pytest.
        orig_stdout = sys.stdout
        sys.stdout = io.StringIO()
        ret_code = pytest.main(["-x", self.path.replace("exercises / ", "tests / test_")])
        sys.stdout = orig_stdout
        return Result(ret_code)

    def state(self) -> State:
        """
        Returns the state of the exercise.
        """
        with open(self.path, encoding="UTF-8") as source_code:
            while line := source_code.readline():
                if "# I AM NOT DONE" in line.rstrip():
                    return State.PENDING
        return State.DONE

    def is_done(self) -> bool:
        """
        Checks if the exercise is done.
        """
        return self.state() == State.DONE

    def is_correct(self) -> bool:
        """
        Checks if the exercise is correct.
        """
        return self.run().is_success()


class Exercises:
    def __init__(self):
        """
        Loads the exercises information.
        """
        with open("resources/info.toml", "rb") as f:
            exercises_toml = load(f)
        self.exercises: list = []
        self.exercises_dict: dict[str, Exercise] = {}

        for exercise in exercises_toml["exercises"]:
            _exercise = Exercise(**exercise)

            self.exercises_dict[exercise["name"]] = _exercise
            self.exercises.append(_exercise)

    def all(self) -> list[Exercise]:
        return self.exercises

    def __getitem__(self, name: str) -> Exercise:
        return self.exercises_dict[name]
