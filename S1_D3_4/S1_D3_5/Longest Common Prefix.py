def longest_common_prefix(strings):
    prefix = ""
    for i in range(len(strings[0])):
        char = strings[0][i]
        for string in strings[1:]:
            if i >= len(string) or string[i] != char:
                return prefix
        prefix += char

    return prefix

# Example usage:
words = ["flower","flow","flight"]
print(longest_common_prefix(words))
