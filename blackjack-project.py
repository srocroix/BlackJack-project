#======================
# BLACKJACK by srocroix
#======================
import random

# 52 deck cards (13 cards by suit) data:

deck = []

clubs = [['Ace', 'Clubs', 11], ['2', 'Clubs', 2], ['3', 'Clubs', 3], ['4', 'Clubs', 4], ['5', 'Clubs', 5], ['6', 'Clubs', 6], ['7', 'Clubs', 7], ['8', 'Clubs', 8], ['9', 'Clubs', 9], ['10', 'Clubs', 10], ['Jack', 'Clubs', 10], ['Queen', 'Clubs', 10], ['King', 'Clubs', 10]]
diamonds = [['Ace', 'Diamonds', 11], ['2', 'Diamonds', 2], ['3', 'Diamonds', 3], ['4', 'Diamonds', 4], ['5', 'Diamonds', 5], ['6', 'Diamonds', 6], ['7', 'Diamonds', 7], ['8', 'Diamonds', 8], ['9', 'Diamonds', 9], ['10', 'Diamonds', 10], ['Jack', 'Diamonds', 10], ['Queen', 'Diamonds', 10], ['King', 'Diamonds', 10]]
hearts = [['Ace', 'Hearts', 11], ['2', 'Hearts', 2], ['3', 'Hearts', 3], ['4', 'Hearts', 4], ['5', 'Hearts', 5], ['6', 'Hearts', 6], ['7', 'Hearts', 7], ['8', 'Hearts', 8], ['9', 'Hearts', 9], ['10', 'Hearts', 10], ['Jack', 'Hearts', 10], ['Queen', 'Hearts', 10], ['King', 'Hearts', 10]]
spades = [['Ace', 'Spades', 11], ['2', 'Spades', 2], ['3 of Spades', 3], ['4', 'Spades', 4], ['5', 'Spades', 5], ['6', 'Spades', 6], ['7', 'Spades', 7], ['8', 'Spades', 8], ['9', 'Spades', 9], ['10', 'Spades', 10], ['Jack', 'Spades', 10], ['Queen', 'Spades', 10], ['King', 'Spades', 10]]

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

shuffle(shoe)
# WARNING: The last 60 to 75 cards won't be used (the plastic insert card must be placed before them)

# print(deck)
print(shoe)
