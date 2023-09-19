import random

word_list = ['ardvark', 'baboon', 'camel']

random_index = random.randint(0, len(word_list) - 1)
random_word = word_list[random_index]
max_attempts = 6
incorrect_guesses = 0

# Initialize blanks as a list of underscores with the same length as the selected word
blanks = ['_'] * len(random_word)

# Convert random_word to lowercase for case-insensitive matching
random_word = random_word.lower()

# Gallows visualization
gallows = [
    """
     +---+
     |   |
         |
         |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
         |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
     |   |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|   |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
    /    |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    =========
    """
]

print("Welcome to Hangman!")
while '_' in blanks and incorrect_guesses < max_attempts:
    display_gallows = gallows[incorrect_guesses]
    print(display_gallows)
    print(" ".join(blanks))
    
    guess_user = input('Ask the user to guess a letter:').lower()

    if len(guess_user) == 1 and guess_user.isalpha():  # Check if the input is a single letter
        correct_guess = False  # Flag to check if the guess is correct

        for i in range(len(random_word)):
            if random_word[i] == guess_user:
                blanks[i] = guess_user  # Replace the underscore with the correct letter
                correct_guess = True

        if correct_guess:
            print('Right!')
        else:
            print('Wrong!')
            incorrect_guesses += 1

    else:
        print('Please enter a single letter.')

if '_' not in blanks:
    print('Congratulations! You guessed the word:', random_word)
else:
    print('You ran out of attempts. The word was:', random_word)
    print(gallows[incorrect_guesses])  # Display the full gallows if the player loses
