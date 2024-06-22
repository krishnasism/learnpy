# Problem: Fix the while loop

# List of words to concatenate
words = ["Hello", "world", "this", "is", "a", "test"]
expected_result = "Hello world this is a test"

# This variable should store the concatenated string
actual_result = ""
index = 0

while index <= len(words):
    index += 1
    actual_result += words[index] + " "

actual_result = actual_result.strip()

# When you are done with an exercise, remove the following line!
# I'M NOT DONE

assert expected_result == actual_result, f"Expected result to be '{expected_result}', but got '{actual_result}'"
print("ok")
