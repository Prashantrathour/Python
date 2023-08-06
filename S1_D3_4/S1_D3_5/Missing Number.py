def find_missing_number(nums):
    n = len(nums) + 1  # Length of the expected sequence
    expected_set = set(range(1, n + 1))  # Create a set of the expected sequence
    actual_set = set(nums)  # Create a set of the given numbers
    missing_number = expected_set - actual_set

    return missing_number.pop()

# Example usage:
numbers = [3, 0, 2, 1]
missing = find_missing_number(numbers)
print("The missing number is:", missing)
