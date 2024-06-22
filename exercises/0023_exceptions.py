# Problem: Handle exception


def divide_numbers(a, b):
    result = None
    try:
        result = a / b
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed")
    return result


numerator = 10
denominator = 0

# TODO: Make sure output is correct
expected_message = "Denominator cannot be 0"
actual_message = ""
try:
    result = divide_numbers(numerator, denominator)
except IndexError:
    actual_message = "index error"


# When you are done with an exercise, remove the following line!
# I'M NOT DONE

assert actual_message == expected_message, f"Expected {expected_message} got {actual_message}"
print("ok")
