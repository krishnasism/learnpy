# Problem: Fix the if-else-if statement

science = 45
history = 55
art = 40

actual_result = ""


average_score = (science + history + art) / 3

if average_score >= 50:
    actual_result = "Pass"
elif average_score >= 70:
    actual_result = "Pass with Distinction"
else:
    actual_result = "Fail"

# When you are done with an exercise, remove the following line!
# I'M NOT DONE

# To get a hint, change the following no to a yes
# hint: no

# Tests - don't update
expected_result = "Fail"

assert expected_result == actual_result, "Expected to fail"
print("ok")
