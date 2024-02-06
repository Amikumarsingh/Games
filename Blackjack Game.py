logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
print(logo)
print("Welcome to online Blackjack game...")
import random
def deal_card():
    '''Return a random card from the deck'''
    cards = [ 11 ,2 , 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def compare(user_score , computer_score):
    if user_score > 21 and computer_score > 21:
        return "You went over. You lose 😤"
    if user_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "Lose, opponent has blackjack"
    elif user_score == 0:
        return "Win with a blackjack"
    elif user_score>21:
        return "You went over. You loose"
    elif computer_score > 21:
        return "Opponent went over. You win"
    elif user_score> computer_score:
        return "You win"
    else:
        return  "you loose"

def play_game():

    user_cards = []
    computer_card = []
    is_game_over = False

    for _ in range(2):
        new_card = deal_card()
        user_cards.append(new_card)
        compu_card = deal_card()
        computer_card.append(compu_card)

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_card)
        print(f"   Your cards: {user_cards}, current score: {user_score}")
        print(f"   Computer's first card: {computer_card[0]}")

        while computer_score != 0 and computer_score < 17:
            computer_card.append(deal_card())
            computer_score = calculate_score(computer_card)

        print(f" Your final hand: {user_cards}, final score: {user_score} ")
        print(f" Computer's free hand: {computer_card}, final score: {computer_score}")
        print(compare(user_score, computer_score))

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True


while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
  'cls'
  play_game()

