def read_words_from_file(filename):
    word_list = []
    with open(filename, 'r') as file:
        for line in file:
            word = line.strip()  # Remove leading/trailing whitespaces and newlines
            word_list.append(word)
    return word_list

# Usage example
file_path = 'C:\Python Bootcamp\Day 5\Hangman\words.txt'  # Replace with the actual file path
words = read_words_from_file(file_path)


