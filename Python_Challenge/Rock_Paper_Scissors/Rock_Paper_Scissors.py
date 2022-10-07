import random

gameRuning = True
user = str(input("What is your choice ? 'r' for rock, 'p' for paper, 's' for scissors:"))
computer = random.choice(['r', 'p', 's'])

def play():
    global gameRuning
#   user = input("What is your choice ? 'r' for rock, 'p' for paper, 's' for scissors:")
#   computer = random.choice(['r', 'p', 's'])

    # while gameRuning:
    #     if errorChecker(user):
    #         return "Invalid Input"
    #     else:
    #         continue
        

    if user == computer:
        return "It's a tie"
    
    if is_win(user, computer):
        return "You Won!!!"
    

    elif is_win(computer, user):
        return "You lost!!!"

    
# r > s, s > p, p > r

#def is_win(player, opponent):
    #return True if the player wins
    # r > s, s > p, p > r
#    if (player == "r" and opponent == "s") or (player == "s" and opponent == "p" ) or (player == "p" and opponent == "r"):
#            return True

def is_win(user, computer):
    #return True if the player wins
    if (user == "r" and computer == "s") or (user == "s" and computer == "p" ) or (user == "p" and computer == "r"):
            return True
    elif (computer == "r" and user == "s") or (computer == "s" and user == "p" ) or (computer == "p" and user == "r"):
            return True

# def errorChecker(user):
#     global gameRuning
#     while gameRuning:
#         if (user != "r" ) or (user != "s" ) or (user != "p" ):
#             return "Invalid Input"
#         else:
#             continue
    
        
#errorChecker(user) 
print(play())
