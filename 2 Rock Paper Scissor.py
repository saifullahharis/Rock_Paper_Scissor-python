# project No2

import random

user_wins = 0
computer_wins = 0

options = ["R", "P", "S"]

while True:
    user_input = input("""
    please type....
    R for Rock
    P for Paper
    S for Scissors or 
    Q to quit: """).upper()
    if user_input == "Q":
        break

    if user_input not in options:
        print("please choose a valid charector next time")
        continue

    random_number = random.randint(0,2)  #Rock:0, Paper:1, Scissor:2
    computer_pick = options[random_number]
    print("computer picked", computer_pick + ".")

    if user_input == "R" and computer_pick == "S":
        print("you won!")
        user_wins += 1
    elif user_input == "P" and computer_pick == "R":
        print("you won!")
        user_wins += 1
    elif user_input == "S" and computer_pick == "P":
        print("you won!")
        user_wins += 1
    else:
        print("You lost!")
        computer_wins += 1

print("You won", user_wins, "times.")
print("The computer won", computer_wins, "times.")
