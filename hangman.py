# Hangman Game code
hangman_code = '''
import random

def hangman():
    words = ["python", "code", "alpha", "hangman", "project"]
    word = random.choice(words)
    guessed_letters = []
    attempts = 6

    print("Welcome to Hangman!")
    print("_ " * len(word))

    while attempts > 0:
        guess = input("Guess a letter: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            print("Please enter a single alphabetical character.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print("Good guess!")
        else:
            print("Wrong guess!")
            attempts -= 1

        display_word = [letter if letter in guessed_letters else "_" for letter in word]
        print(" ".join(display_word))
        print(f"Attempts left: {attempts}")

        if "_" not in display_word:
            print("Congratulations! You guessed the word.")
            break
    else:
        print(f"Out of attempts! The word was '{word}'. Better luck next time.")

if __name__ == "__main__":
    hangman()
'''

# Write to the hangman.py file
hangman_path = "/mnt/data/CodeAlpha_Projects/Hangman_Game/hangman.py"
with open(hangman_path, "w") as file:
    file.write(hangman_code)

hangman_path
