# Problem: Fix the class

# Class representing a Student
class Student:
    def __init__(self, name):
        self.name = name

    def set_score(self, score):
        self.score = score

    def passed(self):
        return self.score >= 60


def test_student():
    student_name = "Alice"
    student_score = 70

    student = Student(student_name)

    assert student.passed(), f"{student.name} should have passed with a score of {student_score}"


test_student()

# When you are done with an exercise, remove the following line!
# I'M NOT DONE
