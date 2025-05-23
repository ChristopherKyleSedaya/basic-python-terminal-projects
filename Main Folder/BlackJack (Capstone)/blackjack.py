
from art import logo
import random


def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card



def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)


def compare(user_score1, computer_score1):
    if user_score1 == computer_score1:
        return "it's a draw"
    elif computer_score1 == 0:
        return "you lose"
    elif user_score1 == 0:
        return "You win"
    elif user_score1 > 21:
        return "you lose"
    elif computer_score1 > 21:
        return "You win"
    elif user_score1 > computer_score1:
        return "You win"
    else:
        return "you lose"


user_cards = []
computer_cards = []

def playing_game():
    print(logo)
    computer_score = 0
    user_score = 0
    game_over = False


    user_cards.append(deal_card())
    user_cards.append(deal_card())

    computer_cards.append(deal_card())
    computer_cards.append(deal_card())


    while not game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards} Your score:{user_score}")
        print(f"Computer card: {computer_cards[0]}")

        if user_cards == 0:
            game_over = True
        elif computer_cards == 0:
            game_over = True
        elif user_score > 21:
            game_over = True
        else:
            user_choice_card = input("Type y to draw another card type n to let computer play").lower()
            if user_choice_card == "y":
                user_cards.append(deal_card())
            else:
                game_over = True


        while computer_score != 0  and computer_score < 17:
            computer_cards.append(deal_card())
            computer_score = calculate_score(computer_cards)


        print(f"Your hand {user_cards} and score {user_score}")
        print(f"computer's hand {computer_cards} and computer's score {computer_score}")
        print(compare(user_score, computer_score))

while input("Want to play a game of blackjack? y/n") == "y":
    print("\n" * 100)
    playing_game()





