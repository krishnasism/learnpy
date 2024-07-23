# Problem: Fix the while loop

# List of words to concatenate
words = ["Hello", "world", "this", "is", "a", "test"]
expected_result = "Hello world this is a test"

# This variable should store the concatenated string
actual_result = ""
index = 0

# When you are done with an exercise, remove the following line!
# I'M NOT DONE

# To get a hint, change the following no to a yes
# hint: no

# Tests - don't update

while index <= len(words):
    index += 1
    actual_result += words[index] + " "

actual_result = actual_result.strip()

assert actual_result == actual_result, f"Expected {expected_result} got {actual_result}"
print("ok")
