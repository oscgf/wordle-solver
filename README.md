# Wordle Solver

This project is a Python-based **Wordle Solver** that helps users identify possible words for the Wordle game based on their guesses and feedback. Given a 5-letter guessed word and feedback on each letter's correctness, this script refines possible word options until only one word (the solution) remains.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Requirements](#requirements)
- [Usage](#usage)
- [Code Explanation](#code-explanation)
- [License](#license)

## Overview

The Wordle Solver assists players by reducing the potential word list based on user-provided feedback for each guess. Users can input guesses and feedback iteratively, with the program generating a narrowed-down list of possible words until it identifies the target word.

## Requirements

- Python 3.6+
- A file named `dict.txt` containing a list of 5-letter words, each on a new line. This repository includes a Spanish dictionary file based on the work from [this repository](https://github.com/JorgeDuenasLerin/diccionario-espanol-txt/blob/master/0_palabras_todas.txt). The file has been modified to contain only 5-letter words and excludes words with accent marks.


## Usage

1. **Set up the `dict.txt` file**:
   Ensure you have a `dict.txt` file in the same directory as the script. Each line in this file should contain a single 5-letter word in lowercase (e.g., `abeja`, `bravo`, `cable`).

2. **Run the Script**:
   To run the program, execute the following command in your terminal:
   ```bash
   python main.py

3. **Input Word and Feedback**:
   - Enter your guessed 5-letter word.
   - Input the feedback for each letter using:
     - `+` for a correct letter in the correct position.
     - `?` for a correct letter but incorrect position.
     - `-` for an incorrect letter.
   - The program will filter and suggest words based on your input.

4. **Iterate**:
   Continue entering words and feedback until the program suggests the final word.

### Example Run


```plaintext
Enter your guessed word (5 letters): piano
Enter the result (+ for green, ? for yellow, - for gray): -??+-
There are 41 possible words
Suggested next word: tuina
```


## Code Explanation

### Main Functions

1. **`open_dict()`**:
   - Reads words from `dict.txt` and stores them in a list.

2. **`get_feedback_regex(word, result, regex_parts)`**:
   - Generates a regex pattern to exclude, include, or confirm letter positions based on feedback.
   - Produces a regex pattern that helps refine the list of possible words.

3. **`filter_words(word_list, regex)`**:
   - Uses the regex pattern to filter the `word_list`, retaining only words that match the current feedback.

4. **`validate_word_and_result(word, result)`**:
   - Ensures user input is valid, checking that:
     - The guessed word is alphabetic and 5 characters long.
     - The feedback is exactly 5 characters long and only includes `+`, `?`, or `-`.

5. **`wordle_solver(word_list)`**:
   - The main function where user inputs are taken, validated, and processed until the final word is found or suggested.

## License

This project is open source and available under the MIT License.