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
    include_letters = []
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
            include_letters.append(char)
        elif feedback == '-':  # Gray - letter not in word
            regex_parts[i] = regex_parts[i][:-1] + exclude_letters + ']' if regex_parts[i] is not None else f"[^{exclude_letters}]"

    # Join regex parts
    include_parts = [f"(?=.*{letter})" for letter in include_letters]
    include_pattern = ''.join(include_parts)
    regex_pattern = ''.join(regex_parts)
    regex_pattern = f'^{include_pattern}{regex_pattern}$'

    return regex_pattern, regex_parts


def filter_words(word_list, regex):
    """Filter the word list using the given regex pattern."""
    pattern = re.compile(regex)
    return [word for word in word_list if pattern.match(word)]


def validate_word_and_result(word: str, result: str) -> bool:
    """
    Validates that 'word' is a 5-letter alphabetic string and
    'result' is a 5-character string containing only '+', '?', or '-'.
    """
    if len(word) != 5 or len(result) != 5:
        print("Please enter valid inputs (5 letters and 5 results).")
        return False
    elif not word.isalpha():
        print("The word should contain only letters.")
        return False
    elif not re.fullmatch(r"[+\-?]{5}", result):
        print("The result should contain only the characters +, ?, and -.")
        return False
    return True


def wordle_solver(word_list):
    """Main function to solve the Wordle puzzle."""
    regex_parts = [None] * 5

    while True:
        word = input("Enter your guessed word (5 letters): ").strip().lower()
        result = input("Enter the result (+ for green, ? for yellow, - for gray): ").strip()

        if not validate_word_and_result(word, result):
            continue

        # Generate regex pattern based on input
        regex, regex_parts = get_feedback_regex(word, result, regex_parts)
        # Filter words
        possible_words = filter_words(word_list, regex)

        # Output the results
        if len(possible_words) > 5:
            print(f"There are {len(possible_words)} possible words")
            print("Suggested next word: ", random.choice(possible_words))
        elif len(possible_words) == 1:
            print("The final word is: ", possible_words[0])
            exit(1)
        else:
            print("Possible words: ", possible_words)


if __name__ == "__main__":
    # Read words from dict.txt
    words = open_dict()
    # Play wordle
    wordle_solver(words)
