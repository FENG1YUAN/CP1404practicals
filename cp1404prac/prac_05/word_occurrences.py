"""
CP1404/CP5632 - Practical
FENG YUAN

Word Occurrences Analysis
Estimate: 15 minutes
Actual: 13 minutes
Pseudo-code:

The program starts with the main function where it prompts the user for an input text.

The provided text is then split into individual words.

A dictionary named word_count is initialized to store the count of each word.

For each word in the split words:
The word's count is incremented in the word_count dictionary. If the word isn't already in the dictionary,
it's initialized with a count of 1.

To ensure proper formatting while displaying:
The program determines the length of the longest word in the word_count dictionary.

The dictionary is then sorted based on the words (keys).

Finally, the program displays each word along with its count, with the word column being aligned based on the length
of the longest word.
"""


def main():
    """Analyze and display the occurrence of each word in a given text."""
    text = input("Text: ")
    words = text.split()
    word_count = {}

    for word in words:
        word_count[word] = word_count.get(word, 0) + 1

    longest_word = max(word_count, key=len)
    max_length = len(longest_word)

    sorted_words = sorted(word_count.items())

    for word, count in sorted_words:
        print(f"{word:{max_length}} : {count}")


if __name__ == '__main__':
    main()
