# Problem: Fix the for loop

numbers = [1, 2, 3, 4, 5]
expected_sum = 15

# This variable should store the result of summing the numbers
actual_sum = 0

for i in range(len(numbers) + 1):
    actual_sum += numbers[i]

# When you are done with an exercise, remove the following line!
# I'M NOT DONE

assert expected_sum == actual_sum, f"Expected sum to be {expected_sum}, but got {actual_sum}"
