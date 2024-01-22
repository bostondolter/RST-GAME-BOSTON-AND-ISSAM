# Program 1 - BlackJack

This is a program that simulates the card game of blackjack, also called 21. 
The goal of the game is to get as close to 21 value as possible without going over and busting. 
The player competes against the dealer, who follows a fixed set of rules.

# How to play

To start the game, run `python blackjack.py` in your terminal.
The program will deal two cards to the player and the dealer, and show the player's cards and one of the dealer's cards.
The player can choose to hit (get another card) or stand (end their turn) by typing `h` or `s` in the terminal.
The player can hit as many times as they want, but if their total points exceed 21, they bust and lose the game.
The dealer will hit until their total points are 17 or higher, or they bust.
If neither the player nor the dealer busts, the one with the higher total points wins the game. If they have the same total points, it is a tie.
The program will show the final cards and points of both the player and the dealer, and the outcome of the game.
The program will ask the player if they want to play again by typing `y` or `n` in the terminal.

# Rules
The cards 2 through 10 have their face value, the face cards (J, Q, K) are worth 10 points, and the ace can be worth 1 or 11 points, depending on the player's choice.
If the player has an ace and their total points are 11 or less, they have a soft hand, and the ace is worth 11 points. If their total points are 12 or more, they have a hard hand, and the ace is worth 1 point.
If the player or the dealer has a blackjack (an ace and a 10-point card) as their first two cards, they win the game automatically, unless the other also has a blackjack, in which case it is a tie.
The player can only split their hand if they have two cards of the same value, and they can only do it once. Splitting means dividing the hand into two separate hands, and playing each hand individually.
The player can only double down their bet if they have a hard 9, 10, or 11 as their first two cards. Doubling down means doubling the initial bet and getting only one more card.
The player can only surrender their hand if they have a hard 15, 16, or 17 as their first two cards. Surrendering means giving up half of the initial bet and ending the game.
