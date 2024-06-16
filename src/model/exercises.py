from tomllib import load

from .exercise import Exercise


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
