# Problem: Fix the conditional assignment using the ternary operator

age = 16
has_license = False

actual_result = (
    "Eligible to drive" if age >= 18 or has_license else "Eligible to drive" if age >= 16 else "Not eligible to drive"
)


# When you are done with an exercise, remove the following line!
# I'M NOT DONE

# To get a hint, change the following no to a yes
# hint: no

# Tests - don't update
expected_result = "Not eligible to drive"

assert expected_result == actual_result, "Expected to be not eligible to drive"
print("ok")
