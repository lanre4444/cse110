# Word Puzzle Game
# Creativity Added:
# I added random secret word selection from a list of words,
# so the game is different each time the player runs the program.

import random

# LIST OF POSSIBLE SECRET WORDS
words = ["mosiah", "temple", "python", "journey", "kingdom"]

# RANDOMLY CHOOSE A SECRET WORD
secret_word = random.choice(words)

print("Welcome to the word guessing game!")
print()

# DISPLAY INITIAL HINT
print("Your hint is: ", end="")

for letter in secret_word:
    print("_ ", end="")

print()
    
# VARIABLES
guess = ""
guess_count = 0

# MAIN GAME LOOP
while guess != secret_word:

    print()

    # USER GUESS
    guess = input("What is your guess? ").lower()

    # COUNT EVERY GUESS
    guess_count += 1

    # CHECK LENGTH
    if len(guess) != len(secret_word):
        print("Sorry, the guess must have the same number of letters as the secret word.")

    else:

        # BUILD HINT
        hint = ""

        # LOOP THROUGH EACH LETTER
        for i in range(len(secret_word)):

            # EXACT MATCH = UPPERCASE
            if guess[i] == secret_word[i]:
                hint += guess[i].upper() + " "

            # LETTER EXISTS BUT WRONG POSITION = LOWERCASE
            elif guess[i] in secret_word:
                hint += guess[i].lower() + " "

            # LETTER NOT PRESENT = UNDERSCORE
            else:
                hint += "_ "

        # DISPLAY HINT ONLY IF GUESS IS WRONG
        if guess != secret_word:
            print("Your hint is:", hint)

# GAME FINISHED
print()
print("Congratulations! You guessed it!")
print(f"It took you {guess_count} guesses.")