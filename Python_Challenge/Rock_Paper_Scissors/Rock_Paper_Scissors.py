
import random
gameRunning = True


user=input("What is your choice ? 'r' for rock, 'p' for paper, 's' for scissors:")
computer = random.choice(["r","p","s"])
while (user != "r") and (user != "p") and (user != "s"):
    print("Invalid input, try again")
    user=input("What is your choice ? 'r' for rock, 'p' for paper, 's' for scissors:")

else:
    print("You have seclected :", user,"The computer has selected:",computer)

def play():
    if user == computer:
        return "It's a tie"
    if is_win(user, computer):
        return "You won"
    else:
        return("You lost, The computer whipped your ass boa!!!")
   

def is_win(user, computer):
    #r > s, s > p, p > r
    if(user == "r" and computer == "s") or (user == "s" and computer == "p") or (user == "p" and computer == "r"):
        return True

print(play())