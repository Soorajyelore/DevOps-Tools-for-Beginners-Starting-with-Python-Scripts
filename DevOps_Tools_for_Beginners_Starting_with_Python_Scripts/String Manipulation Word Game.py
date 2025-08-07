from anaconda_project.internal.conda_api import result
from zmq.backend import second


def word_game(input_word=None):
    # Get a word from the user or use the provided input
    if input_word is None:
        word = input("Enter a word: ")
    else:
        word = input_word

    # Task 1: Find the length of the word
    # Your code here

    # Task 2: Print the word and its length
    # Your code here

    # Task 3: Reverse the word
    # Your code here

    # Task 4: Print the reversed word
    # Your code here

    # Task 5: Create a new word by repeating the first character
    # Your code here

    # Task 6: Print the new word
    # Your code here

    # Task 7: Concatenate the original word with a suffix
    # Your code here

    # Task 8: Print the word with suffix
    # Your code here

    # Task 9: Convert the word to uppercase
    # Your code here

    # Task 10: Print the uppercase word
    # Your code here

    # Task 11: Replace a character in the word
    # Your code here

    # Task 12: Print the word with replaced character
    # Your code here

if __name__ == "__main__":
    word_game()

# Hints:
# - Use len() function to find the length of a string
# - Use string slicing with a step of -1 to reverse a string
# - Use the * operator for string repetition
# - Use the + operator for string concatenation
# - Use the upper() method to convert a string to uppercase
# - Use the replace() method to replace characters in a string
# - Use f-strings for formatted output

