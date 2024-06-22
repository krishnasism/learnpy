# Problem: Fix the while loop

# List of words to concatenate
words = ["Hello", "world", "this", "is", "a", "test"]
expected_result = "Hello world this is a test"

# This variable should store the concatenated string
actual_result = ""
index = 0

while index <= len(words):
    actual_result += words[index] + " "
    index += 1

actual_result = actual_result.strip()

assert expected_result == actual_result, f"Expected result to be '{expected_result}', but got '{actual_result}'"

# When you are done with an exercise, remove the following line!
# I'M NOT DONE
