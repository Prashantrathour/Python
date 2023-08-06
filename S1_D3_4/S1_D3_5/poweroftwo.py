def is_power_of_two(n):
    if n <= 0:
        return False

    return (n & (n - 1)) == 0

# Example usage:
num1 = 4
num2 = 7

print(num1, "is a power of two:", is_power_of_two(num1))  # Output: True
print(num2, "is a power of two:", is_power_of_two(num2))  # Output: False
print(num2 &(num2-1))


# explanation
# n     = 100 (in binary)
# n - 1 = 011 (in binary)
# -----------------
# n & (n - 1) = 000
