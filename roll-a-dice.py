import random
response = "y"
def roll_dice():
    return random.randint(1, 6)
while response == "y":
    no = roll_dice()

    if no == 1:
        print("---------")
        print("|       |")
        print("|   0   |")
        print("|       |")
        print("---------")
    elif no == 2:
        print("---------")
        print("|       |")
        print("|0     0|")
        print("|       |")
        print("---------")
    elif no == 3:
        print("---------")
        print("|       |")
        print("|0  0  0|")
        print("|       |")
        print("---------")
    elif no == 4:
        print("---------")
        print("| 0   0 |")
        print("|       |")
        print("| 0   0 |")
        print("---------")
    elif no == 5:
        print("---------")
        print("| 0   0 |")
        print("|   0   |")
        print("| 0   0 |")
        print("---------")
    elif no == 6:
        print("---------")
        print("| 0 0 0 |")
        print("|       |")
        print("| 0 0 0 |")
        print("---------")

    response = input("Do you want to roll the dice again? Enter 'y' for yes and 'n' for exiting.")

print("Thanks for playing.")