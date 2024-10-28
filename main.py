import re
import random


def open_dict():
    try:
        with open("dict.txt", "r") as file:
            # Read the words and strip any whitespace
            words = [line.strip().lower() for line in file]
    except FileNotFoundError:
        print("Error: dict.txt file not found. Please ensure it exists in the same directory as this script.")
        exit(1)
    return words


def get_feedback_regex(word, result, regex_parts):
    """Generate a regex pattern based on the guessed word and result."""
    exclude_letters = ""
    # First loop to calculate the letters to be excluded
    for i, char in enumerate(word):
        feedback = result[i]

        if feedback == '-':  # Gray - letter not in word
            exclude_letters += char

    # Second loop to generate or update the regex
    for i, char in enumerate(word):
        feedback = result[i]    

        if feedback == '+':  # Green - correct letter and position
            regex_parts[i] = char
        elif feedback == '?':  # Yellow - correct letter but wrong position
            regex_parts[i] = regex_parts[i][:-1] + exclude_letters + char + ']' if regex_parts[i] is not None else f"[^{exclude_letters}{char}]"
        elif feedback == '-':  # Gray - letter not in word
            regex_parts[i] = regex_parts[i][:-1] + exclude_letters + ']' if regex_parts[i] is not None else f"[^{exclude_letters}]"

    # Join regex parts
    regex_pattern = ''.join(regex_parts)
    regex_pattern = f'^{regex_pattern}$'  # Start and end anchors
    print(f"Regex patten: {regex_pattern}")
    return regex_pattern, regex_parts


def filter_words(word_list, regex):
    """Filter the word list using the given regex pattern."""
    pattern = re.compile(regex)
    return [word for word in word_list if pattern.match(word)]


def wordle_solver(word_list):
    """Main function to solve the Wordle puzzle."""
    regex_parts = [None] * 5

    while True:
        word = input("Enter your guessed word (5 letters): ").strip().lower()
        result = input("Enter the result (+ for green, ? for yellow, - for gray): ").strip()

        if len(word) != 5 or len(result) != 5:
            print("Please enter valid inputs (5 letters and 5 results).")
            continue

        # Generate regex pattern based on input
        regex, regex_parts = get_feedback_regex(word, result, regex_parts)
        # Filter words
        possible_words = filter_words(word_list, regex)

        # Output the results
        if len(possible_words) > 5:
            print("Suggested next word: ", random.choice(possible_words))
        else:
            print("Possible words: ", possible_words)


if __name__ == "__main__":
    # Read words from dict.txt
    words = open_dict()
    # Play wordle
    wordle_solver(words)
