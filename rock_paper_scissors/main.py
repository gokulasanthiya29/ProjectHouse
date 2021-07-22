import random

user_win = 0
computer_wins = 0

options = ["ROCK", "PAPER", "SCISSORS"]


while True:
    
    user_choice = input('Pick rock/paper/scissors (or) q to quit: ').upper()
    
    if user_choice == "Q":
        break

    if user_choice not in options:
        continue

    random_pick = random.randint(0,1)
    computer_pick = options[random_pick]
    print('Computer picks', computer_pick + '.')
    
    if user_choice == "ROCK" and computer_pick == "SCISSORS":
        print("You won! :) ")
        user_win += 1
    
    elif user_choice == "PAPER" and computer_pick == "ROCK":
        print("You won! :) ")
        user_win += 1
    
    elif user_choice == "SCISSORS" and computer_pick == "PAPER":
        print("You won! :) ")
        user_win += 1
    
    else:
        print("You lost! :( ")
        computer_wins += 1
        
print("You won", user_win, "times against the Computer!")

