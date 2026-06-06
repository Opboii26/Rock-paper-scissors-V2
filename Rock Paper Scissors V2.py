import random

Items = [0, 1, 2]
ItemsName = ["Rock", "Paper", "Scissors"]

Computer = random.choice(Items)
print("Computer has choosed its item!\nChoose between 0, 1, 2.")
Player = int(input("Enter your item: "))

Condition = 0
Conditions = ["Draw", "Win", "Lose"]

match Player:
    case 0:
        Condition = Computer

    case 1:
        match Computer:
            case 0:
                Condition = 2
            case 1:
                Condition = 0
            case 2:
                Condition = 1

    case 2:
        match Computer:
            case 0:
                Condition = 1
            case 1:
                Condition = 2
            case 2:
                Condition = 0

print(f"Computer chose {ItemsName[Computer]}.")

print(Conditions[Condition])