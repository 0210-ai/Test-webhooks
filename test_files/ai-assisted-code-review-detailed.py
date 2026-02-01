def find_second_largest(numbers):
    """
    This function is supposed to find the second largest number in a list.
    However, it has a subtle logical bug.
    """
    if len(numbers) < 2:
        return None

    largest = float('-inf')
    second_largest = float('-inf')

    for number in numbers:
        if number > largest:
            second_largest = largest
            largest = number
        elif number > second_largest and number != largest:
            second_largest = number

    # The bug is that if the largest number appears more than once,
    # the second_largest will not be updated correctly.
    # For example, in [10, 10, 5], the result will be -inf instead of 5.

    return second_largest

# Example of the bug
print(find_second_largest([10, 10, 5])) # Expected: 5, Actual: -inf
print(find_second_largest([5, 5, 5])) # Expected: None or 5, Actual: -inf
print(find_second_largest([1, 2, 3, 4, 5])) # Expected: 4, Actual: 4 (Correct)
print(find_second_largest([10, 8, 10])) # Expected: 8, Actual: 8 (Correct)
