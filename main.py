# Jan 16, 2024
# Boston Dolter and Issam Syed

# BlackJack

# import pygame program
# import random
import copy
import random
import pygame

pygame.init()

# Create cards so that random picks it
cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
one_deck = 4 * cards
decks = 4
WIDTH, HEIGHT = 800, 400  # Adjusted initial size for better visibility
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption('Blackjack! By Issam and Boston')
fps = 60
timer = pygame.time.Clock()
font = pygame.font.Font('freesansbold.ttf', 28)
smaller_font = pygame.font.Font('freesansbold.ttf', 24)
active = False
# win, loss, draw/push
records = [0, 0, 0]
player_score = 0
dealer_score = 0
initial_deal = False
my_hand = []
dealer_hand = []
outcome = 0
reveal_dealer = False
hand_active = False
outcome = 0
add_score = False
results = ['', 'You BUSTED', 'Let\'s Go, You Actually Won', 'DEALER WINS, You Suck', 'Push (TIE)']

# Deal cards by selecting randomly from the deck, and make a function for one card at a time
def deal_cards(current_hand, current_deck):
    card = random.randint(0, len(current_deck))
    current_hand.append(current_deck[card - 1])
    current_deck.pop(card - 1)
    return current_hand, current_deck

# Draw scores for the player and dealer on the screen
def draw_scores(player, dealer):
    screen.blit(font.render(f'Your Score: {player}', True, 'white'), (10, 10))
    if reveal_dealer:
        screen.blit(font.render(f'Dealer Score: {dealer}', True, 'white'), (10, 40))

# Draw cards visually onto the screen
def draw_cards(player, dealer, reveal):
    for i in range(len(player)):
        pygame.draw.rect(screen, 'white', [10 + (50 * i), 200 + (3 * i), 80, 120], 0, 5)
        screen.blit(font.render(player[i], True, 'black'), (15 + 50 * i, 205 + 3 * i))
        screen.blit(font.render(player[i], True, 'black'), (15 + 50 * i, 275 + 3 * i))
        pygame.draw.rect(screen, 'red', [10 + (50 * i), 200 + (3 * i), 80, 120], 5, 5)

    # If the player hasn't finished the turn, the dealer will hide one card
    for i in range(len(dealer)):
        pygame.draw.rect(screen, 'white', [10 + (50 * i), 50 + (3 * i), 80, 120], 0, 5)
        if i != 0 or reveal:
            screen.blit(font.render(dealer[i], True, 'black'), (15 + 50 * i, 55 + 3 * i))
            screen.blit(font.render(dealer[i], True, 'black'), (15 + 50 * i, 125 + 3 * i))
        else:
            screen.blit(font.render('???', True, 'black'), (15 + 50 * i, 55 + 3 * i))
            screen.blit(font.render('???', True, 'black'), (15 + 50 * i, 125 + 3 * i))
        pygame.draw.rect(screen, 'blue', [10 + (50 * i), 50 + (3 * i), 80, 120], 5, 5)

# Pass in player or dealer hand and get the best score possible
def calculate_score(hand):
    # Calculate the hand score fresh every time, check how many aces we have
    hand_score = 0
    aces_count = hand.count('A')
    for i in range(len(hand)):
        # For 2,3,4,5,6,7,8,9 - just add the number to the total
        for j in range(8):
            if hand[i] == cards[j]:
                hand_score += int(hand[i])
        # For 10 and face cards, add 10
        if hand[i] in ['10', 'J', 'Q', 'K']:
            hand_score += 10
        # For aces, start by adding 11; we'll check if we need to reduce afterward
        elif hand[i] == 'A':
            hand_score += 11
    # Determine how many aces need to be 1 instead of 11 to get under 21 if possible
    if hand_score > 21 and aces_count > 0:
        for i in range(aces_count):
            if hand_score > 21:
                hand_score -= 10
    return hand_score

# Draw game conditions and buttons
def draw_game(act, record, result, button_size):
    button_list = []
    # Initially on startup (not active), the only option is to deal a new hand
    if not act:
        deal = pygame.draw.rect(screen, 'white', [WIDTH // 4, HEIGHT // 1.3, WIDTH // 2, HEIGHT // 8], 0, 5)
        pygame.draw.rect(screen, 'green', [WIDTH // 4, HEIGHT // 1.3, WIDTH // 2, HEIGHT // 8], 3, 5)
        deal_text = font.render('DEAL HAND', True, 'black')
        screen.blit(deal_text, (WIDTH // 4 + 15, HEIGHT // 1.3 + 30))
        button_list.append(deal)
    # Once the game started, show hit and stand buttons and win/loss records
    else:
        button_width, button_height = button_size
        hit = pygame.draw.rect(screen, 'white', [WIDTH // 4, HEIGHT // 1.5, button_width, button_height], 0, 5)
        pygame.draw.rect(screen, 'green', [WIDTH // 4, HEIGHT // 1.5, button_width, button_height], 3, 5)
        hit_text = font.render('HIT ME', True, 'black')
        screen.blit(hit_text, (WIDTH // 4 + 15, HEIGHT // 1.5 + 25))
        button_list.append(hit)
        stand = pygame.draw.rect(screen, 'white', [WIDTH // 2, HEIGHT // 1.5, button_width, button_height], 0, 5)
        pygame.draw.rect(screen, 'green', [WIDTH // 2, HEIGHT // 1.5, button_width, button_height], 3, 5)
        stand_text = font.render('STAND', True, 'black')
        screen.blit(stand_text, (WIDTH // 2 + 15, HEIGHT // 1.5 + 25))
        button_list.append(stand)
        score_text = smaller_font.render(f'Wins: {record[0]}   Losses: {record[1]}   Draws: {record[2]}', True, 'white')
        screen.blit(score_text, (10, HEIGHT - 30))
    # If there is an outcome for the hand that was played, display a restart button and tell the user what happened
    if result != 0:
        screen.blit(font.render(results[result], True, 'white'), (10, 10))
        # Center the "NEW HAND" button
        button_width, button_height = button_size
        button_x = (WIDTH - button_width) // 2
        button_y = HEIGHT // 1.5 + 50  # Adjust the vertical position as needed

        deal = pygame.draw.rect(screen, 'white', [button_x, button_y, button_width, button_height], 0, 5)
        pygame.draw.rect(screen, 'green', [button_x, button_y, button_width, button_height], 3, 5)
        pygame.draw.rect(screen, 'black', [button_x + 3, button_y + 3, button_width - 6, button_height - 6], 3, 5)
        deal_text = font.render('NEW HAND', True, 'black')
        screen.blit(deal_text, (button_x + 15, button_y + 20))  # Adjust the text position as needed
        button_list.append(deal)
    return button_list

# Check endgame conditions function
def check_endgame(hand_act, deal_score, play_score, result, totals, add):
    # Check end-game scenarios if the player has stood, busted, or blackjack
    # Result 1- player bust, 2-win, 3-loss, 4-push
    if not hand_act and deal_score >= 17:
        if play_score > 21:
            result = 1
        elif deal_score < play_score <= 21 or deal_score > 21:
            result = 2
        elif play_score < deal_score <= 21:
            result = 3
        else:
            result = 4
        if add:
            if result == 1 or result == 3:
                totals[1] += 1
            elif result == 2:
                totals[0] += 1
            else:
                totals[2] += 1
            add = False
    return result, totals, add

# Main game loop
run = True
while run:
    timer.tick(fps)

    # Event handling, if quit pressed, then exit the game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.MOUSEBUTTONUP:
            if not active:
                if buttons[0].collidepoint(event.pos):
                    active = True
                    initial_deal = True
                    game_deck = copy.deepcopy(decks * one_deck)
                    my_hand = []
                    dealer_hand = []
                    outcome = 0
                    hand_active = True
                    reveal_dealer = False
                    outcome = 0
                    add_score = True
            else:
                # If the player can hit, allow them to draw a card
                if buttons[0].collidepoint(event.pos) and player_score < 21 and hand_active:
                    my_hand, game_deck = deal_cards(my_hand, game_deck)
                # Allow the player to end turn (stand)
                elif buttons[1].collidepoint(event.pos) and not reveal_dealer:
                    reveal_dealer = True
                    hand_active = False
                elif len(buttons) == 3:
                    if buttons[2].collidepoint(event.pos):
                        active = True
                        initial_deal = True
                        game_deck = copy.deepcopy(decks * one_deck)
                        my_hand = []
                        dealer_hand = []
                        outcome = 0
                        hand_active = True
                        reveal_dealer = False
                        outcome = 0
                        add_score = True
                        dealer_score = 0
                        player_score = 0

    # If the player busts, automatically end the turn - treat it like a stand
    if hand_active and player_score >= 21:
        hand_active = False
        reveal_dealer = True

    outcome, records, add_score = check_endgame(hand_active, dealer_score, player_score, outcome, records, add_score)

    pygame.display.flip()

pygame.quit()
