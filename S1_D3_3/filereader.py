def count_words(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            word_count = len(content.split())
            return word_count
    except FileNotFoundError:
        print("Error: File not found.")
        return 0

def write_word_count_to_file(word_count, output_filename):
    with open(output_filename, 'w') as file:
        file.write("Number of words is"+str(word_count))

if __name__ == "__main__":
    input_filename = "test.txt"
    output_filename = "output.txt"

    word_count = count_words(input_filename)
    print(f"Number of words in the file: {word_count}")

    write_word_count_to_file(word_count, output_filename)
    print(f"Word count written to {output_filename}.")
