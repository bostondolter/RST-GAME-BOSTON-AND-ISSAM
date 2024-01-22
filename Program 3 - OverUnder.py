# Program 3 - OverUnder guess the number 1 - 1000

import random

# Function to pick a number 1 - 1000
def generate_number():
    return random.randint(1, 1000)

# Function to compare the guess with correst number and give feedback whether its over or under
def compare_guess(guess, number):
    if guess == number: # If the guess is correct
        return 'You got it!' # Return a message
    elif guess > number: # If your guess is too high
        return 'Too high. Try again.' # Return a message
    else: # If your guess is too low
        return 'Too low. Try again.' # Return a message

print('Welcome to Over Under!') # Introduces the game
number = generate_number() # Generates a random number
guesses = 0 # Number of guesses
guessed = False # indicates if the player has guessed correctly

while not guessed: # While the player has not guessed correctly
    try:
        guess = int(input('Guess a number between 1 and 1000: ')) # Ask the player for another guess
    except ValueError:
        print('Invalid input. Please enter a number.') # if they enter a character other than a number
    else:
        if guess < 1 or guess > 1000: # Check if the guess is within the range
            print('Out of range. Please enter a number between 1 and 1000.') # Print a message
        else:
            guesses += 1 # Increase the number of guesses by one
            feedback = compare_guess(guess, number) # Get the feedback from the compare_guess function
            print(feedback) # Print the feedback
            if feedback == 'You got it!': # If the feedback is positive
                guessed = True # You guessed correctly
                print('You guessed the number in', guesses, 'guesses.') # print the number of guesses