#======================
# BLACKJACK by srocroix
#======================
import random

# 52 deck cards (13 cards by suit) data:

deck = []

clubs = [['A', 'Ace of Clubs', 11], ['2', '2 of Clubs', 2], ['3', '3 of Clubs', 3], ['4', '4 of Clubs', 4], ['5', '5 of Clubs', 5], ['6', '6 of Clubs', 6], ['7', '7 of Clubs', 7], ['8', '8 of Clubs', 8], ['9', '9 of Clubs', 9], ['10', '10 of Clubs', 10], ['J', 'Jack of Clubs', 10], ['Q', 'Queen of Clubs', 10], ['K', 'King of Clubs', 10]]
diamonds = [['A', 'Ace of Diamonds', 11], ['2', '2 of Diamonds', 2], ['3', 'Diamonds', 3], ['4', '4 of Diamonds', 4], ['5', '5 of Diamonds', 5], ['6', '6 of Diamonds', 6], ['7', '7 of Diamonds', 7], ['8', '8 of Diamonds', 8], ['9', '9 of Diamonds', 9], ['10', '10 of Diamonds', 10], ['J', 'Jack of Diamonds', 10], ['Q', 'Queen of Diamonds', 10], ['K', 'King of Diamonds', 10]]
hearts = [['A', 'Ace of Hearts', 11], ['2', '2 of Hearts', 2], ['3', '3 of Hearts', 3], ['4', '4 of Hearts', 4], ['5', '5 of Hearts', 5], ['6', '6 of Hearts', 6], ['7', '7 of Hearts', 7], ['8', '8 of Hearts', 8], ['9', '9 of Hearts', 9], ['10', '10 of Hearts', 10], ['J', 'Jack of Hearts', 10], ['Q', 'Queen of Hearts', 10], ['K', 'King of Hearts', 10]]
spades = [['A', 'Ace of Spades', 11], ['2', '2 of Spades', 2], ['3', '3 of Spades', 3], ['4', '4 of Spades', 4], ['5', '5 of Spades', 5], ['6', '6 of Spades', 6], ['7', '7 of Spades', 7], ['8', '8 of Spades', 8], ['9', '9 of Spades', 9], ['10', '10 of Spades', 10], ['J', 'Jack of Spades', 10], ['Q', 'Queen of Spades', 10], ['K', 'King of Spades', 10]]

deck.extend(clubs)
deck.extend(diamonds)
deck.extend(hearts)
deck.extend(spades)
# print(deck)

# Set how many decks containsare in the shoe:

shoe = 8 * deck
# print(shoe)

# Shuffle function definition:

def shuffle(list_to_shuffle):
    return random.shuffle(list_to_shuffle)


game_running = True

# NEW GAME LOOP:


# WARNING: The last 60 to 75 cards won't be used (the plastic insert card must be placed before them)

while game_running == True:

    trash_shoe = []
    dealer_hand = []
    player_hand = []
    dealer_score = []
    player_score = []
    hitting_card = True

    print("\n==============================")
    print("==============================")
    print("N E W   G A M E   L A U N C H")
    print("==============================")
    print("==============================")

    shuffle(shoe)

    # Dealing cards:
    dealer_hand.append(shoe.pop(0)) # one card face up for dealer
    player_hand.append(shoe.pop(0)) # one card face up for player
    dealer_hand.append(shoe.pop(0)) # one card face down for dealer
    player_hand.append(shoe.pop(0)) # one card face up for player

    dealer_score = dealer_hand[0][-1] + dealer_hand[1][-1]
    player_score = player_hand[0][-1] + player_hand[1][-1]
    print("\nDealer's hand:", dealer_hand[0][1], "/ Hidden Card")
    print('Dealer Score:', dealer_score)
    print("\nYour hand:", player_hand[0][1], "/", player_hand[1][1])
    print('Your Score:', player_score)
    print("\n==============================")
   
    while hitting_card == True:
        whats_next_handle = input("\nWhat's your next move?\na) Hit b) Stand\n")
        whats_next = whats_next_handle.lower()
        if whats_next == "a":
            print("\nYou Hit!" + "\nDealing card...\n")
            print("==============================")
            player_hand.append(shoe.pop(0))  # hit one card face up for player
            player_score += player_hand[-1][-1] # update of player score
            print("\nYour hand:", player_hand)
            print("Your Score:", player_score)
            print("\nDealer's hand:", dealer_hand[0][1], "/ Hidden Card")
            print('Dealer Score:', dealer_score)
        else:
            hitting_card = False
            break
        continue
        
    # Results display:

    print("\nFinal Result\n")
    print("Your Score:", player_score, "/", player_hand)
    print("Dealer Score:", dealer_score, "/", dealer_hand)

    if player_score > dealer_score:
        print("==============================")
        print("C O N G R A T S !")
        print("Y O U   W O N !")
        print("==============================")
    elif player_score == dealer_score:
        print("==============================")
        print("I T ' S   A   D R A W ...")
        print("==============================")
    else:
        print("==============================")
        print("D E A L E R   W O N !")
        print("==============================\n")
    
    continue