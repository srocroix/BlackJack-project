#================================
# BLACKJACK SIMULATOR by srocroix
#================================
import random
import time
from decimal import Decimal

# 52 deck cards (13 cards by suit) data:

deck = []

clubs = [['A', 'Ace of Clubs', 11], ['2', '2 of Clubs', 2], ['3', '3 of Clubs', 3], ['4', '4 of Clubs', 4], ['5', '5 of Clubs', 5], ['6', '6 of Clubs', 6], ['7', '7 of Clubs', 7], ['8', '8 of Clubs', 8], ['9', '9 of Clubs', 9], ['10', '10 of Clubs', 10], ['J', 'Jack of Clubs', 10], ['Q', 'Queen of Clubs', 10], ['K', 'King of Clubs', 10]]
diamonds = [['A', 'Ace of Diamonds', 11], ['2', '2 of Diamonds', 2], ['3', '3 of Diamonds', 3], ['4', '4 of Diamonds', 4], ['5', '5 of Diamonds', 5], ['6', '6 of Diamonds', 6], ['7', '7 of Diamonds', 7], ['8', '8 of Diamonds', 8], ['9', '9 of Diamonds', 9], ['10', '10 of Diamonds', 10], ['J', 'Jack of Diamonds', 10], ['Q', 'Queen of Diamonds', 10], ['K', 'King of Diamonds', 10]]
hearts = [['A', 'Ace of Hearts', 11], ['2', '2 of Hearts', 2], ['3', '3 of Hearts', 3], ['4', '4 of Hearts', 4], ['5', '5 of Hearts', 5], ['6', '6 of Hearts', 6], ['7', '7 of Hearts', 7], ['8', '8 of Hearts', 8], ['9', '9 of Hearts', 9], ['10', '10 of Hearts', 10], ['J', 'Jack of Hearts', 10], ['Q', 'Queen of Hearts', 10], ['K', 'King of Hearts', 10]]
spades = [['A', 'Ace of Spades', 11], ['2', '2 of Spades', 2], ['3', '3 of Spades', 3], ['4', '4 of Spades', 4], ['5', '5 of Spades', 5], ['6', '6 of Spades', 6], ['7', '7 of Spades', 7], ['8', '8 of Spades', 8], ['9', '9 of Spades', 9], ['10', '10 of Spades', 10], ['J', 'Jack of Spades', 10], ['Q', 'Queen of Spades', 10], ['K', 'King of Spades', 10]]

deck.extend(clubs)
deck.extend(diamonds)
deck.extend(hearts)
deck.extend(spades)
# print(deck)

# Set how many decks containsare in the shoe:

num_of_decks = 6
shoe = num_of_decks * deck
# print(shoe)
trash_shoe = []

# Shuffle function definition:

def shuffle(shoe_list):
    return random.shuffle(shoe_list)

def custom_time_sleep(sec):
    if robot_activated == False:
        time.sleep(sec)

def double_line():
    print("\n==============================")

robot_activated = None
robot_num_of_games = 0
game_running = True
soft_17_hit = None
game_count = 0
winrate = 0
winning_count = 0
losing_count = 0
dealer_blackjack_count = 0
player_blackjack_count = 0
draw_count = 0
basic_bet_value = 0
bet_value = 0
total_bet_value = 0
casino_wallet = 0
highest_bet = 0
bet_auto_activated = False
my_money = 0
my_money_final = 0
losing_money_index = 0
bet_strategy = False

hit = "a"
stand = "b"
double_down = "c"

strategy_alembert_pyramid = False
strategy_martingale = False
strategy_inverted_martingale = False
strategy_custom_martingale = False
strategy_custom_alembert_pyramid = False
strategy_piquemouche_martingale = False
strategy_custom_piquemouche_martingale = False

last_game_blackjack = 0
last_game_win = 0
last_game_lose = 0
last_game_draw = 0
winning_loop = 0
losing_loop = 0
big_losing_loop = 0
double_down_counter = 0
won_double_down_counter = 0

new_game_settings = True

hi_lo_counter_running_count = 0
hi_lo_counter_true_count = 0
insert_end_card = random.uniform(60, 75)

top_winning_loop = 0
top_losing_loop = 0

shuffle(shoe)

# Game Loop:

while game_running == True:

    dealer_hand = []
    player_hand = []
    player_hand_split_A = []
    player_hand_split_B = []

    dealer_score = 0
    player_score = 0
    ace_in_hand = 0
    dealer_ace_in_hand = 0
    double_down_bet = 0

    hitting_card = True
    player_bust = False
    dealer_bust = False
    double_down_status = False
    ace_face_up_card = False
    player_black_jack = False
    dealer_black_jack = False
    
    def new_card_for_player():
        player_hand.append(shoe.pop(0))  # one card for player

    def calculate_player_score():
        global player_score
        player_score = 0
        global ace_in_hand
        ace_in_hand = 0
        for card in player_hand:
            player_score += card[-1]
            if card[0] == 'A':
                ace_in_hand += 1
        for card in player_hand:
            if card[0] == 'A' and player_score > 21 and ace_in_hand > 0:
                player_score -= 10
        return player_score

    def split_cards():
        player_hand_split_A = player_hand[0]
        player_hand_split_B = player_hand[1]
        
    def new_card_for_dealer():
        dealer_hand.append(shoe.pop(0))  # one card for dealer

    def calculate_dealer_score():
        global dealer_score
        dealer_score = 0
        global dealer_ace_in_hand
        dealer_ace_in_hand = 0
        for card in dealer_hand:
            dealer_score += card[-1]
            if card[0] == 'A':
                dealer_ace_in_hand += 1
        for card in dealer_hand:
            if card[0] == 'A' and dealer_score > 21 and dealer_ace_in_hand > 0:
                dealer_score -= 10
        return dealer_score

    def your_hand():
        print('\nYour hand:')
        for card in list(player_hand):
            print(card[1])
        print("Your Score:", calculate_player_score())


    def deal_hand_face_down():
        calculate_dealer_score()
        print('\nDealer hand:')
        print(dealer_hand[0][1])
        print('"Face Down Card"')
        print('Dealer Score:', dealer_hand[0][-1])


    def deal_hand():
        print('\nDealer hand:')
        for card in list(dealer_hand):
            print(card[1])
        print('Dealer Score:', calculate_dealer_score())
    
    def four_five_rule():
        rule_check = False
        if len(player_hand) >= 3 and player_hand == 16 and dealer_hand == 10:
            for card in player_hand:
                if card[-1] == 4 or card[-1] == 5:
                    rule_check == True
        return rule_check

    def hi_lo_cards_counting():
        global hi_lo_counter_running_count
        for card in player_hand:
            card_value = card[-1]
            if card_value < 7 and card_value != 1:
                hi_lo_counter_running_count += 1
            elif card_value == 10 or card_value == 11 or card_value == 1:
                hi_lo_counter_running_count -= 1
            else:
                pass
        for card in dealer_hand:
            card_value = card[-1]
            if card_value < 7 and card_value != 1:
                hi_lo_counter_running_count += 1
            elif card_value == 10 or card_value == 11:
                hi_lo_counter_running_count -= 1
            else:
                pass
        
    print("\n==============================")
    print("♤ ♥ ♦ ♧ ♤ ♥ ♦ ♧ ♤ ♥ ♦ ♧ ♤ ♥ ♦")
    print("==============================")
    print("\nN E W   G A M E   L A U N C H")
    print("\n==============================")
    print("♤ ♥ ♦ ♧ ♤ ♥ ♦ ♧ ♤ ♥ ♦ ♧ ♤ ♥ ♦")
    print("==============================")

    # New game settings:

    if game_count == 0 or new_game_settings == True:

        while my_money_final <= 0 or bet_value > my_money_final :
            print("\nYour account is empty!")
            try:
                my_money_handle = input("\nHow much money do you want to add on your casino account?\n\n")
                my_money = float(my_money_handle)
                my_money_final = my_money
            except:
                print("\nPlease enter a number.\n(Avoid any letters or special caracters)")
                continue
        
        while soft_17_hit == None:
            try:
                soft_17_hit_handle = input("\nWhat's the dealer move on soft 17?\na) He stands\nb) He hits\n\n")
                soft_17_hit_input = soft_17_hit_handle.lower()

                if soft_17_hit_input == "a":
                    soft_17_hit = True
                elif soft_17_hit_input == "b":
                    soft_17_hit = False
            except:
                print("\nPlease enter a valid answer.\n(Input 'A' or 'B'\n")
                continue
        
        while robot_activated == None:
            
            running_robot_hande = input("\nDo you want to run the robot or play manually?\na) Run the Robot\nb) Play manually\n\n")
            running_robot_input = running_robot_hande.lower()
        
            if running_robot_input == "a":
                robot_activated = True

            elif running_robot_input == "b":
                robot_activated = False
                bet_auto_handle = input("\nDo you want to turn on auto bet?\na) Yes\nb) No\n\n")
                bet_auto_input = bet_auto_handle.lower()
    
                if bet_auto_input == "a":
                    bet_auto_activated = True
                    bet_value_handle = input("\nHow much do you want to bet?\n\n")
                    basic_bet_value = float(bet_value_handle)
                elif bet_auto_input != "a" or bet_auto_input == "b":
                    bet_auto_activated = False
            else:
                print("\nPlease enter a valid answer!")
                continue
    
        if bet_auto_activated == True or robot_activated == True:
            bet_strategy_handle = input("\nDo you want to use a bet strategy?\na) Yes\nb) No\n\n(Note: If you answer 'Yes' by taping 'a' key, the robot will play ofr you!)\n\n")
            bet_strategy_input = bet_strategy_handle.lower()

            if bet_strategy_input == "a":
                while bet_strategy == False:
                    pick_strategy_handle = input("\nWhat strategy would you like to use?\na) Martingale\nb) Alembert Pyramid\nc) Custom Martingale\nd) Inverted Martingale\ne) Custom Alembert Pyramid\nf) Piquemouche Martingale (WIP)\n\n")
                    pick_strategy_input = pick_strategy_handle.lower()

                    if pick_strategy_input == "a":
                        print("\nMartingale Strategy selected!")
                        strategy_martingale = True
                        bet_strategy = True
                    elif pick_strategy_input == "b":
                        print("\nAlembert Pyramid Strategy selected!")
                        strategy_alembert_pyramid = True
                        bet_strategy = True
                    elif pick_strategy_input == "c":
                        print("\nCustom Martingale Strategy selected!")
                        strategy_custom_martingale = True
                        bet_strategy = True
                    elif pick_strategy_input == "d":
                        print("\nInverted Martingale Strategy selected!")
                        strategy_inverted_martingale = True
                        bet_strategy = True
                    elif pick_strategy_input == "e":
                        print("\nCustom Alembert Pyramid Strategy selected!")
                        strategy_custom_alembert_pyramid = True
                        bet_strategy = True
                    elif pick_strategy_input == "f":
                        print("\nPiquemouche Martingale Strategy selected!")
                        strategy_piquemouche_martingale = True
                        bet_strategy = True
                    else:
                        print("\nYou didn't pick any bet strategy!\nPlease enter a valid answer.")
                        bet_strategy = False
                        continue
                
            else:
                print("\nYou didn't pick any bet strategy!\nThe Bet strategy system is turned off.")
                bet_strategy = False

        if robot_activated == True:
            while robot_num_of_games == 0:
                try:
                    robot_num_of_games_handle = input("\nHow many games do you want the robot to play?\n\n")
                    robot_num_of_games = int(robot_num_of_games_handle)
                except:
                    print("\nPlease enter a number.\n(Avoid any letters or special caracters)")
                    continue

            while basic_bet_value == 0 or basic_bet_value > my_money_final:
                try:
                    bet_value_handle = input("\nHow much do you want the robot to bet?\n\n")
                    basic_bet_value = float(bet_value_handle)

                    if basic_bet_value > my_money_final:
                        print("\nYou can't bet so much!\nYou only have", my_money_final, "€ on your account.")
                        continue

                except:
                    print("\nPlease enter a number.\n(Avoid any letters or special caracters)")
                    continue
    
    new_game_settings = False

    if bet_auto_activated == False and robot_activated == False:
        while basic_bet_value == 0:
            try:
                bet_value_handle = input("\nHow much do you want to bet?\n\n")
                basic_bet_value = float(bet_value_handle)
            except:
                print("\nPlease enter a number.\n(Avoid any letters or special caracters)")
                continue

    my_money = Decimal(my_money)
    my_money = round(my_money, 2)

    my_money_final = Decimal(my_money_final)
    my_money_final = round(my_money_final, 2)

    basic_bet_value = Decimal(basic_bet_value)
    basic_bet_value = round(basic_bet_value, 2)

    bet_value = Decimal(bet_value)
    bet_value = round(bet_value, 2)
    
    # Betting Strategies Rules:

    if strategy_martingale == True:
        if game_count == 0:
            bet_value = basic_bet_value
        if last_game_lose > 0 and last_game_draw == 0 and last_game_win == 0:
            bet_value = bet_value * 2
        elif last_game_win > 0:
            bet_value = basic_bet_value
        elif last_game_draw > 0:
            pass
        else:
            bet_value = basic_bet_value

    elif strategy_alembert_pyramid == True:
        if game_count == 0:
            bet_value = basic_bet_value
        elif last_game_draw == 0 and winning_loop > 0:
                bet_value -= basic_bet_value
        elif last_game_draw == 0 and losing_loop > 0:
            bet_value += basic_bet_value

    elif strategy_inverted_martingale == True:
        if game_count == 0:
            bet_value = basic_bet_value
        if (winning_loop % 2) == 0 and last_game_draw == 0:
            bet_value = basic_bet_value * 2
        
    elif strategy_custom_martingale == True:
        if (game_count == 0) or (last_game_draw == 0 and winning_loop > 0):
            bet_value = basic_bet_value
        elif last_game_draw == 0 and losing_loop > 0:
            bet_value += basic_bet_value

    elif strategy_custom_alembert_pyramid == True:
        if (game_count == 0) or (last_game_draw == 0 and winning_loop > 0):
            bet_value = basic_bet_value
        elif last_game_draw == 0 and losing_loop > 0:
            bet_value += basic_bet_value

    elif strategy_piquemouche_martingale == True:
        if game_count == 0:
            bet_value = basic_bet_value
        if last_game_draw == 0:
            if losing_loop >= 1:
                losing_money_index += bet_value
            if winning_loop >= 1:
                losing_money_index -= bet_value
            if (losing_loop % 3) == 0 and losing_money_index > bet_value:
                bet_value = bet_value * 2
            if losing_money_index <= bet_value:
                bet_value = basic_bet_value
            if bet_value > (basic_bet_value * 32):
                bet_value = basic_bet_value

    elif strategy_custom_piquemouche_martingale == True:
        if game_count == 0:
            bet_value = basic_bet_value
            # Work in Progress

    elif bet_strategy == False:
        bet_value = basic_bet_value
    
    custom_time_sleep(0.5)
    print("\nBank Account:", my_money_final, "€")
    print("\nYou bet", bet_value, "€")
    my_money_final -= bet_value
    custom_time_sleep(0.5)
    print("\nBank Account:", my_money_final, "€")

    custom_time_sleep(0.5)
    print("\nWait a few seconds...")
    custom_time_sleep(0.5)
    print("Dealer is dealing cards.")
    custom_time_sleep(0.5)
    double_line()

    # Dealing cards:

    new_card_for_dealer()
    new_card_for_player()
    new_card_for_dealer()
    new_card_for_player()
    
    # Displaying cards:

    deal_hand_face_down()
    your_hand()

    dealer_face_up_card_value = int(dealer_hand[0][-1])
    first_player_card_value = int(player_hand[0][-1])
    second_player_card_value = int(player_hand[1][-1])
    
    # BlackJack checking:

    if dealer_hand[0][0] == 'A':
        ace_face_up_card = True
        if dealer_score == 21:
            dealer_black_jack = True
            dealer_blackjack_count += 1
            print("\nDealer has a BlackJack!")

    if player_score == 21:
        player_black_jack = True
        player_blackjack_count +=1
        print("\nYou have a BlackJack!")

    double_line()
    
    # Player / Robot move:

    while hitting_card == True and player_score < 21:
        if ace_face_up_card == True and dealer_black_jack == True:
            break
        if player_black_jack == True:
            break
        custom_time_sleep(0.5)
        if robot_activated == False and len(player_hand) == 2:
            whats_next_handle = input("\nWhat's your next move?\na) Hit\nb) Stand\nc) Double Down (x2)\n\n")
            whats_next = whats_next_handle.lower()
        elif robot_activated == False and len(player_hand) > 2:
            whats_next_handle = input("\nWhat's your next move?\na) Hit\nb) Stand\n\n")
            whats_next = whats_next_handle.lower()
                
        # Robot rules:

        if robot_activated == True:

            if player_score < 9:
                whats_next = hit
            if player_score < 12 and len(player_hand) > 2:
                whats_next = hit
            if len(player_hand) == 2 and player_score < 12:
                whats_next = hit
            if (len(player_hand) == 2 and player_score == 9) and (dealer_face_up_card_value >= 3 and dealer_face_up_card_value <= 6):
                if bet_strategy == False:
                    whats_next = double_down
                elif bet_strategy == True:
                    whats_next = hit
            if (len(player_hand) == 2 and player_score == 10) and (dealer_face_up_card_value >= 2 and dealer_face_up_card_value <= 9):
                if bet_strategy == False:
                    whats_next = double_down
                elif bet_strategy == True:
                    whats_next = hit
            if (len(player_hand) == 2 and player_score == 11) and (dealer_face_up_card_value >= 2 and dealer_face_up_card_value <= 10):
                if bet_strategy == False:
                    whats_next = double_down
                elif bet_strategy == True:
                    whats_next = hit
            
            if (ace_in_hand != 1 and player_score == 12) and (dealer_face_up_card_value == 2 or dealer_face_up_card_value == 3 or dealer_face_up_card_value >= 7):
                whats_next = hit
            if (ace_in_hand != 1 and player_score == 12 and len(player_hand) == 2) and (first_player_card_value == 10 or first_player_card_value == 2) and (dealer_face_up_card_value == 4):
                whats_next = hit
            if (ace_in_hand != 1 and player_score == 12) and (first_player_card_value != 10 or first_player_card_value != 2) and (dealer_face_up_card_value == 4):
                whats_next = stand
            if (ace_in_hand != 1 and player_score == 12) and (dealer_face_up_card_value == 5 or dealer_face_up_card_value == 6):
                whats_next = stand

            if (ace_in_hand != 1 and player_score > 12 and player_score < 17) and (dealer_face_up_card_value < 7):
                whats_next = stand
            if ace_in_hand != 1 and dealer_face_up_card_value >= 7:
                whats_next = hit

            if ace_in_hand != 1 and four_five_rule() == True:
               whats_next = stand
            
            if ace_in_hand != 1 and player_score > 16:
                whats_next = stand

            if ace_in_hand == 1 and player_score > 12 and player_score < 18 and len(player_hand) == 2:
                whats_next = hit
            if (ace_in_hand == 1 and player_score == 18 and len(player_hand) == 2) and (dealer_face_up_card_value > 8):
                whats_next = hit
            if (ace_in_hand == 1) and (player_score == 19 or player_score == 20) and (len(player_hand)) == 2:
                whats_next = stand
            
        # Player / Robot hitting logic:

        if whats_next == hit:
            double_line()
            print("\nYou Hit!")
            double_line()
            custom_time_sleep(0.5)
            print("\nDealing cards...")
            custom_time_sleep(1)
            new_card_for_player()
            print("\nYou got a", player_hand[-1][1])
            custom_time_sleep(1)
            double_line()
            deal_hand_face_down()
            your_hand()
            double_line()

            if player_black_jack == True:
                print("It's a BlackJack!")

            if player_score == 21:
                hitting_card = False

            if player_score > 21:
                custom_time_sleep(1)
                hitting_card = False
                player_bust = True
                print("\nYou bust!")
                custom_time_sleep(1)

        # Player / Robot standing logic:

        elif whats_next == stand: 
            hitting_card = False
            double_line()
            print("\nYou Stand!")
            double_line()

        # Player / Robot Double Down logic:

        elif whats_next == double_down:
            hitting_card = False
            double_down_status = True
            double_down_counter += 1
            double_down_bet = bet_value * 2
            my_money_final -= bet_value
            double_line()
            print("\nYou Double your bet!")
            print("\nYour total bet value is", double_down_bet, "€")
            double_line()
            custom_time_sleep(0.5)
            print("\nDealing cards...")
            custom_time_sleep(1)
            new_card_for_player()
            print("\nYou got a", player_hand[-1][1])
            custom_time_sleep(1)
            double_line()
            deal_hand_face_down()
            your_hand()
            double_line()

            if player_score > 21:
                custom_time_sleep(1)
                player_bust = True
                print("\nYou bust!")
                custom_time_sleep(1)

    # Dealer move:

    custom_time_sleep(0.5)
    deal_hand()
    if dealer_black_jack == True:
        dealer_blackjack_count += 1
        print("\nDealer has a BlackJack!")
    
    while dealer_bust == False and player_black_jack == False:

        if (dealer_score < 17) or (soft_17_hit == True and dealer_score == 17 and dealer_ace_in_hand == 1):
            custom_time_sleep(0.5)
            double_line()
            print("\nDealer Hits!\n")
            double_line()
            custom_time_sleep(1)
            new_card_for_dealer()
            print("\nDealer got a", dealer_hand[-1][1])
            custom_time_sleep(0.5)
            double_line()
            deal_hand()
        
        
        elif dealer_score > 21:
            custom_time_sleep(0.5)
            dealer_bust = True
            double_line()
            print("\nDealer busts!")
            custom_time_sleep(0.5)
            break

        else:
            custom_time_sleep(0.5)
            double_line()
            print("\nDealer stands.")
            custom_time_sleep(0.5)
            break
                
    # Results rules:

    custom_time_sleep(0.5)
    double_line()
    print("\nFinal Result")
    double_line()
    deal_hand()
    your_hand()

    custom_time_sleep(1)
    if (player_score > dealer_score and player_bust == False and player_black_jack == False) or (player_bust == False and dealer_bust == True and player_black_jack == False):
        winning_count += 1
        last_game_win += 1
        last_game_blackjack = 0
        last_game_draw = 0
        last_game_lose = 0
        winning_loop += 1
        losing_loop = 0
        
        if double_down_status == False:
            my_money_final += bet_value * 2
            double_line()
            print("\nC O N G R A T S !")
            print("Y O U   W O N !")
            print("\nYou won:", (bet_value * 2), "€")
            double_line()
        elif double_down_status == True:
            won_double_down_counter += 1
            my_money_final += double_down_bet * 2
            double_line()
            print("\nC O N G R A T S !")
            print("Y O U   W O N !")
            print("\nYou won:", (double_down_bet * 2), "€")
            double_line()
        


    elif (player_score == dealer_score and dealer_black_jack == False and player_bust == False) or (player_black_jack == True and dealer_black_jack == True):
        draw_count += 1
        last_game_draw += 1
        last_game_blackjack = 0
        last_game_win = 0
        last_game_lose = 0

        if double_down_status == False:
            my_money_final += bet_value
            double_line()
            print("\nI T ' S   A   D R A W ...")
            print("\nYou won:", bet_value, "€")
            double_line()
        elif double_down_status == True:
            my_money_final += double_down_bet
            double_line()
            print("\nI T ' S   A   D R A W ...")
            print("\nYou won:", double_down_bet, "€")
            double_line()

    elif (dealer_score > player_score and dealer_bust == False) or (player_black_jack == False and dealer_black_jack == True) or (player_bust == True):
        losing_count += 1
        last_game_lose += 1
        last_game_blackjack = 0
        last_game_win = 0
        winning_loop = 0
        losing_loop += 1
        last_game_draw = 0
        double_line()
        print("\nD E A L E R   W O N !")
        double_line()
        

    elif player_black_jack == True and dealer_black_jack == False:
        winning_count += 1
        benefit = float(bet_value) * 2.5
        benefit = Decimal(benefit)
        # benefit = round(benefit, 2)
        my_money_final += benefit
        last_game_blackjack += 1
        last_game_win += 1
        last_game_draw = 0
        last_game_lose = 0
        double_line()
        print("\nC O N G R A T S !") 
        print("Y O U   W O N !")
        print("\nYou won:", benefit, "€")
        double_line()
        winning_loop += 1
        losing_loop = 0

    # Results Display:

    game_count += 1

    if highest_bet < bet_value:
        highest_bet = bet_value

    if highest_bet < double_down_bet:
        highest_bet = double_down_bet

    if double_down_status == False:
        total_bet_value += bet_value
    elif double_down_status == True:
        total_bet_value += double_down_bet

    if winning_loop > top_winning_loop:
        top_winning_loop = winning_loop
    if losing_loop > top_losing_loop:
        top_losing_loop = losing_loop
    if losing_loop == 6 and last_game_draw == 0:
        big_losing_loop += 1

    try:
        winrate = (winning_count) / (game_count - draw_count) * 100
        winrate = Decimal(winrate)
        winrate = round(winrate, 2)
    except:
        winrate = 0

    custom_time_sleep(0.5)
    
    hi_lo_cards_counting()
    deck_left = len(shoe) / 52
    deck_left = Decimal(deck_left)
    deck_left = round(deck_left, 2)
    hi_lo_counter_true_count = int(hi_lo_counter_running_count) / int(deck_left)
    print("\nHi-Lo Counter - RC:", hi_lo_counter_running_count)
    print("Deck(s) left in the shoe:", deck_left)
    print("Hi-Lo Counter - TC:", int(hi_lo_counter_true_count))
    # check ace_in _hand variable:
    # print("\nAce in hand:", ace_in_hand) 
    print("\nBank Account:", my_money_final, "€")
    print("Gain/Loss:", (my_money_final - my_money), "€")
    print("Total bet placed:", total_bet_value, "€")
    print("\nTotal Games:", game_count)
    print("Winrate*:", winrate, "%")
    print("Number of Double Down:", double_down_counter)
    print("\nCurrent Winning Loop:", last_game_win)
    print("Current Losing Loop:", last_game_lose)
    print("\nTop Winning Loop:", top_winning_loop)
    print("Top Losing Loop:", top_losing_loop)
    print("Number of Big Losing Loops:", big_losing_loop)

    if robot_activated == True:
        print("\nRobot Mode: ON")
        if strategy_alembert_pyramid == True:
            print("Betting Strategy: Alembert Pyramid")
        elif strategy_custom_martingale == True:
            print("Betting Strategy: Custom Martingale")
        elif strategy_martingale == True:
            print("Betting Strategy: Martingale")
        elif strategy_custom_alembert_pyramid == True:
            print("Betting Strategy: Custom Alembert Pyramid")
        elif strategy_piquemouche_martingale == True:
            print("Betting Strategy: Piquemouche Martingale")
        else:
            print("Betting Strategy: None")
    else:
        print("\nRobot Mode: OFF")
    
    print("Highest Bet registered:", highest_bet, "€")

    print("\nTotal Win:", winning_count)
    print("Total Lose:", losing_count)
    print("Total Draw:", draw_count)
    print("\nTotal Dealer BJ:", dealer_blackjack_count)
    print("Total Player BJ:", player_blackjack_count)
    print("\n*Draws not included.")
    double_line()
    custom_time_sleep(0.5)

    custom_time_sleep(0.5)
    print("\nWait a few seconds...")
    custom_time_sleep(0.5)
    print("\nDealer is picking up the cards...")
    
    trash_shoe.extend(dealer_hand)
    trash_shoe.extend(player_hand)
    custom_time_sleep(0.5)
    print("\nNumber of cards in the shoe:", len(shoe))
    print("Number of cards in the trash shoe:", len(trash_shoe))

    # If the shoe has less than 60 to 75 cards left, we take a new shoe that we shuffle:

    if len(shoe) < insert_end_card:
        shoe.clear()
        trash_shoe.clear()
        shoe = num_of_decks * deck
        shuffle(shoe)
        print("\nPlastic insert card out!")
        custom_time_sleep(0.5)
        print("Reshuffling...")
        hi_lo_counter_running_count = 0
        insert_end_card = random.uniform(60, 75)

    custom_time_sleep(3)

    if robot_activated == True and (game_count == robot_num_of_games) and my_money_final > 0:
        print("\nRobot status = job done\n")
        test_again_handle = input("\nRun the robot again?\na) Yes\nb) No\nc) New game settings\n\n")
        test_again = test_again_handle.lower()
        if test_again == "a":
            robot_num_of_games += int(robot_num_of_games_handle)
        elif test_again == "c":
            new_game_settings = True
            game_running = True
        else:
            game_running = False
            print("\nBlackJack Simulator is off.\n")
        
            break

    elif my_money_final <= 0:
        game_running = False

    continue
