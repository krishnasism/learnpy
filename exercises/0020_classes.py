# Problem: Fix the class


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        area = 3.14 * radius * radius
        return area


def test_circle():
    radius = 5
    expected_area = 78.5

    circle = Circle(radius)

    actual_area = circle.calculate_area()

    assert expected_area == actual_area, f"Expected area to be {expected_area}, but got {actual_area}"


test_circle()

# When you are done with an exercise, remove the following line!
# I'M NOT DONE
