# Program 2 - HangMan

import random

# Wordbank
words = ['school', 'hockey', 'football', 'soccer', 'apple', 'boxing', 'racing', 'chicken', 'skateboard', 'train']

# Picks word randomly from wordbank
def choose_word():
    return random.choice(words)
# Displays word with blanks using underscores (pig = _ _ _)
def display_word(word, guessed):
    display = '' # Empty string to store the display
    for letter in word: # For each letter in the word
        if letter in guessed: # If the letter has been guessed
            display += letter + ' ' # Add the letter and a space to the display
        else: # If the letter has not been guessed
            display += '_ ' # Add a blank and a space to the display
    return display

# Function to check if the player has won or lost
def check_status(word, guessed, lives):
    if '_' not in display_word(word, guessed): # If there are no blanks in the display
        return 'win' # The player has won
    elif lives == 0: # If the player has no lives left
        return 'lose' # The player has lost
    else: # Otherwise
        return 'continue' # The game continues

# Main game logic
print('Welcome to Hangman by Boston and Issam, try and guess the correct word') # Print a welcome message
word = choose_word() # Choose a random word
guessed = [] # Empty list to store the guessed letters
lives = 6 # Number of lives or limbs on a stickman
status = 'continue' # Game status

while status == 'continue': # While the game is not over
    print('\nYou have', lives, 'lives left.') # Print the number of lives
    print(display_word(word, guessed)) # Print the word with blanks and guessed letters
    guess = input('Guess a letter: ').lower() # Ask the player for a guess and convert it to lowercase
    if len(guess) == 1 and guess.isalpha(): # If the guess is a single letter
        if guess in guessed: # If the guess has already been made
            print('You have already guessed that letter.') # Print a message
        elif guess in word: # If the guess is in the word
            print('Good guess!') # Print a message
            guessed.append(guess) # Add the guess to the guessed list
        else: # If the guess is not in the word
            print('Sorry, that letter is not in the word.') # Print a message
            lives -= 1 # Reduce the lives by one
    else: # If the guess is not a single letter
        print('Invalid input. Please enter a single letter.') # Print a message
    status = check_status(word, guessed, lives) # Update the game status

if status == 'win': # If the player has won
    print('\nCongrats, you won!') # Print a message
    print('The word was', word) # Print the word
elif status == 'lose': # If the player has lost
    print('\nSorry, you have run out of lives.') # Print a message
    print('The word was', word) # Print the correct word