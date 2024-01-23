# Program 1 - BlackJack

This is a program that simulates the card game of blackjack, also called 21. 
The goal of the game is to get as close to 21 value as possible without going over and busting. 
The player competes against the dealer, who follows a fixed set of rules.

# How to play

To start the game, run "blackjack.py" in your terminal.
The program will deal two cards to the player and the dealer, and show the player's cards and one of the dealer's cards.
The player can choose to hit (get another card) or stand (end their turn) pressing the hit or stand button.
The player can hit as many times as they want, but if their total value exceed 21, they bust and lose the game.
The dealer has to hit until their total value is 17 or higher, or they bust.
If both the player the dealer busts, the one with the higher total value wins the game. If they have the same total value, it is a tie or what they call a push.

# Rules
The cards 2 through 10 have their face value, the face cards (J, Q, K) are worth a value of 10, and the ace can be worth 1 or 11 points, depending on the player's choice.
If the player or the dealer has a blackjack (an ace and a card with the value 10) as their first two cards, they win the game automatically, unless the dealer also has a blackjack, in which case it is a push.
