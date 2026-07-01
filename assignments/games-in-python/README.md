# 📘 Assignment: Games in Python

## 🎯 Objective

Build a classic Hangman word-guessing game in Python. You will practice using strings, loops, conditionals, user input, and random selection to create an interactive game.

## 📝 Tasks

### 🛠️	Create the Hangman Game Loop

#### Description
Create a Python program that randomly selects a hidden word and lets the player guess one letter at a time until they win or run out of attempts.

#### Requirements
Completed program should:

- Randomly select one word from a predefined list of at least five words.
- Ask the player to enter a single-letter guess each turn.
- Show the current word progress using underscores for hidden letters, such as `_ _ _`.
- Track and display the number of incorrect guesses remaining.
- End the game when the player guesses the full word or has no attempts left.


### 🛠️	Show Clear Game Results

#### Description
Add feedback so the player understands whether each guess was correct and how the game ended.

#### Requirements
Completed program should:

- Tell the player whether each guessed letter is correct or incorrect.
- Prevent repeated guesses from unfairly reducing the number of remaining attempts.
- Display a winning message when the player reveals the whole word.
- Display a losing message and reveal the hidden word when attempts are exhausted.
- Use clear, student-friendly messages throughout the game.
