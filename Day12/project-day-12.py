import random  # Import the random module to generate a random number

print('Welcome to Number Guessing Game!')
print('I am thinking of a number between 1 and 100.')

choice = input("Choose a difficulty. Type 'easy' or 'hard': ")

# Define a function to play the hard mode
def hard(number_of_attempts=5):
    # Generate a random number between 1 and 100
    target_number = random.randint(1, 100)
    
    print(f'You have {number_of_attempts} attempts remaining to guess the number.')
    
    # Initialize a loop to allow multiple guesses
    while number_of_attempts > 0:
        guess = int(input('Make a guess: '))  # Convert input to an integer
        
        if guess > target_number:
            print('Too high.')
        elif guess < target_number:
            print('Too low.')
        else:
            print(f'Congratulations! You guessed the correct number, which is {target_number}.')
            return  # Exit the function if the guess is correct
        
        number_of_attempts -= 1  # Reduce the number of remaining attempts
    
    print(f'Out of attempts. The correct number was {target_number}.')

# Define a function to play the easy mode
def easy(number=10):
    number1 = random.randint(1, 100)

    print(f'You have {number} attempts remaining to guess the number.')

    while number > 0:
        guess = int(input('Make a guess: '))

        if guess > number1:
            print('Too high')
        elif guess < number1:
            print('Too low')
        else:
            print(f'Congratulations! You guessed the correct number, which is {number1}.')
            return
        
        number -= 1

    print(f'Out of attempts. The correct number was {number1}.')

# Call the hard function to play the game in hard mode
if choice == 'hard':
    hard()
elif choice == 'easy':
    easy()
else:
    print("Invalid choice. Please choose 'easy' or 'hard'.")
