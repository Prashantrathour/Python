

def find_single_element(nums):
    result = 0
    for num in nums:
        result ^= num
    return result

# Example usage:
input_list = [4, 1, 2, 1, 2]
output = find_single_element(input_list)
print(output)
