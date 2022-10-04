
from ast import Break
import random



dice_rolling = True
while dice_rolling:
    num = (random.randint(1,6))

    if num == 1:
        print("---------")
        print("|   0   |")
        print("---------")
        print("YOU GOT ONE")

    if num == 2:
        print("---------")
        print("|   0   |")
        print("|   0   |")
        print("---------")
        print("YOU GOT TWO")

    if num == 3:
        print("-----------")
        print("| 0     0 |")
        print("|    0    |")
        print("-----------")
        print("YOU GOT THREE")

    if num == 4:
        print("---------")
        print("| 0    0 |")
        print("| 0    0 |")
        print("----------")
        print("YOU GOT FOUR")    

    if num == 5:
        print("-----------")
        print("| 0     0 |")
        print("| 0     0 |")
        print("|    0    |")
        print("-----------")
        print("YOU GOT FIVE")

    if num == 6:
        print("-----------")
        print("|  0   0  |")
        print("|  0   0  |")
        print("|  0   0  |")
        print("-----------")
        print("YOU GOT SIX")


    #try:
        another_attempt = str(input("Do you want to to roll the dice again?(y/n):"))
        if another_attempt.lower() == "y":
            continue
        elif another_attempt.lower()=="n":
            break
    #except:
        if another_attempt.lower() is not "y" or "n":
            print("Invalid Input")


