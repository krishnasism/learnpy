# Problem: Fix the if statement

maths = 30
english = 80
sports = 50

expected_pass_result = False

actual_pass_result = True


if (maths + english + sports) / 3 < 50:
    actual_pass_result = True

# When you are done with an exercise, remove the following line!
# I'M NOT DONE

assert expected_pass_result == actual_pass_result, "Expected to fail"
print("ok")
