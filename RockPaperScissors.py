#Rock Papers Scissors

import random

#Randomly generated a # between or at 1 and 3, each move corresponds to an action (R, P, or S)
def computer():
    move = random.randint(1,3)

    if move == 1:
        print("\tComp Move: Rock")
    elif move == 2:
        print("\tComp Move: Paper")
    elif move == 3:
        print("\tComp Move: Scissor")

    return move

#Takes user input, and returns proper n# 
def user_in():
    #asks for user's move and then returns a number coressponding to the move (ie. rock = 1, ...etc.)
    move = input("\nEnter your move: ").upper()

    if move == "R":
        num = 1
        print("\tUser Move: Rock")
    elif move == "P":
        num = 2
        print("\tUser Move: Rock")
    elif move == "S":
        num = 3
        print("\tUser Move: Rock")
    else:
        print("Invalid entry, enter again")
        print()
        num = 4
    return num 


#1 = Rock
#2 = Paper
#3 = Scissors

def compare(user,comp):
    #comp wins 
    if (comp == 1 and user == 3) or (comp == 2 and user == 1) or (comp == 3 and user == 2):
        return 1
    #user wins
    elif (comp == 3 and user == 1) or (comp == 1 and user == 2) or (comp == 2 and user == 3):
        return 0
    else:
        return 2


def num_rounds(wins):
    #number of times user wins
    u = 0 
    #number of times computer wins
    c = 0
    #total number of times played (ties included) 
    i = 0

    print("Wins Needed:",wins)
    
    while (c < wins) and (u < wins):
        i+=1

        #have to do it seperate as it would give error if entry is invalid
        apa = user_in()
        while apa == 4:
            apa = user_in()

        
        num = compare(apa,computer())
        if num == 1:  #computer wins 
            c+=1
        elif num == 0:  #user wins 
            u +=1
        print("\nCurrent Wins:\nUser Wins:",u,"\tComputer Wins:",c)
        

    if c == wins:
        print("\nComupter wins!")
    elif u == wins:
        print("\nYou win!")
    print()
    print("Total # of times played:", i)

            
    

def main():
    print("Welcome to Rock Paper Scissors!\nTo play, enter either R, P, or S for Rock, Paper, or Scissor respectively.")
    print()
    wins = input("Enter how many wins to end game: ")
    while True:
        if not(wins.isnumeric()):
            print("Not a valid entry, enter again")
            wins = input("Enter how many wins to end game: ")
            print()
        else:
            break
    num_rounds(int(wins))

main()
