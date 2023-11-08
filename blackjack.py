from art import logo
import random
import os

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
def clear():
  os.system('cls')
  
def deal_card():
    return random.choice(cards)

def calculate_score(score):
    if sum(score) == 21:
        return 0
    elif 11 in score and sum(score) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(score)

def compare(user_score, computer_score):
    if user_score == 0:
        print("You got a blackjack!")
    elif computer_score == 0:
        print("The computer got a blackjack!")
    elif user_score > 21:
        print("You busted!")
    elif computer_score > 21:
        print("The computer busted!")
    elif user_score == computer_score:
        print("It's a draw!")
    elif user_score > computer_score:
        print("You win!")
    elif computer_score > user_score:
      print("The computer wins!")

choice = input("Do you wanna start playing Blackjack? y/n \n")

def blackjack():
    print(logo)
    game_over = False
    user_cards = []
    computer_cards = []
    user_score = 0
    computer_score = 0
    user_cards.append(deal_card())
    
    while not game_over:
        user_cards.append(deal_card())
        if computer_score < 17:
            computer_cards.append(deal_card())
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's cards: {computer_cards}, computer's score: {computer_score}")
        if user_score == 0 or computer_score == 0 or user_score > 21 or computer_score > 21:
            compare(user_score, computer_score)
            game_over = True
        else:
            draw_card = input("Do you wanna draw another card? y/n \n")
        if draw_card != "y":
            if computer_score < 17:
                computer_cards.append(deal_card())
            computer_score = calculate_score(computer_cards)
            print(f"Your final cards: {user_cards}, final score: {user_score}")
            print(f"Computer's final cards: {computer_cards}, computer's final score: {computer_score}")
            compare(user_score, computer_score)
            game_over = True
    if game_over:
        restart = input("Do you wanna restart the game? y/n \n")
        if restart == "y":
            user_cards.clear()
            clear()
            blackjack()
        else:
            print("Thank you for playing")
        
if choice == "y":
    blackjack()
      