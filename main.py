"""
Rock: -1
Paper: 0
Scissors: 1
"""

"""
Rock vs Paper - Paper wins
Paper vs Scissor - Scissors wins
Scissor vs Rock - Rock wins
"""

import random

computer = random.choice([-1, 0, 1])

print("\n  'ROCK PAPER SCISSORS GAME'  ")
print("\nChoice: 'r': Rock, 'p': Paper, 's': Scissors\n")

user = input("Enter your choice: ")
user_dict = {"r": -1, "p": 0, "s": 1}
user_input = user_dict[user]
reverse_dict = {-1: "Rock", 0: "Paper", 1: "Scissors"}

print(
    f"You chose: {reverse_dict[user_input]}\nComputer chose: {reverse_dict[computer]}"
)

if computer == user_input:
    print("DRAW!!")
else:
    if (computer-user_input==-1) or (computer-user_input==2):
        print("YOU WIN!!\n")
    elif (computer-user_input==1) or (computer-user_input==-2):
        print("YOU LOSE!!\n")
    else:
        print("Something went wrong!!\n")
    
    """if (computer == -1) and (user_input == 0):
        print("You win!!\n")
    elif (computer == 0) and (user_input == 1):
        print("You win!!\n")
    elif (computer == 1) and (user_input == -1):
        print("You win!!\n")
    elif (computer == 0) and (user_input == -1):
        print("You lose!!\n")
    elif (computer == 1) and (user_input == 0):
        print("You lose!!\n")
    elif (computer == -1) and (user_input == 1):
        print("You lose!!\n")
    else:
        print("Something went wrong!!\n")"""
