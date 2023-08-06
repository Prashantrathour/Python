def permutations(s):
    if len(s) == 1:
        return [s]

    result = []
    for i in range(len(s)):
        first_char = s[i]
        remaining_chars = s[:i] + s[i+1:]
        for perm in permutations(remaining_chars):
            result.append(first_char + perm)

    return result

# Example usage:
input_string = "abc"
output = permutations(input_string)
print(output)
