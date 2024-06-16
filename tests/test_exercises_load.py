from src.model.exercises import Exercises


def test_exercises_load():
    # Tests exercises are loaded correctly from info.toml file
    exercises = Exercises()
    assert len(exercises.all()) > 0
