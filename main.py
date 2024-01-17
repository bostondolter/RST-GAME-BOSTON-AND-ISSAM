# Jan 16, 2024
# Boston Dolter and Issam Syed

# BlackJack And Poker


# Python picks a random card
import random
cards = ("Diamonds", "Spades", "Hearts", "Clubs")
ranks = (2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King", "Ace")

def pick_a_card():
    card = random.choices(cards)
    rank = random.choices (ranks)
    return (f"The {rank} of {card}")
print(pick_a_card())