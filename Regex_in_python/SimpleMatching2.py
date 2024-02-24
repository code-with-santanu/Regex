'''
Task:
Create a regular expression pattern that can simultaneously match three words: "abc," "abcd," and "abcde."
The function should return True if all three words are found in the text and False otherwise.
'''
# Import the necessary library
import re


def match_words():
    # Define the regular expression pattern to match
    pattern = r".*"  # pattern = r"abc.*"

    words = ["abc", "abcd", "abcde"]
    # Iterate through each word in the list
    for word in words:
        # Use re.search to check if the pattern is found in the current word
        print(re.search(pattern, word))


if __name__ == "__main__":
    match_words()
