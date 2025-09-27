import sys
import random
from enum import Enum 

def play_rps():

    class RPS(Enum):
        ROCK = 1
        PAPER = 2
        SCISSOR = 3

    
    # print(RPS(2))
    # print(RPS.ROCK)
    # print(["ROCK"])
    # print(RPS.ROCK.value)
    #  sys.exit()



    playerchoice = input("\nEnter... \n1 for Rock, \n2 for Paper, \n3 for Scissor: \n\n ")
    if playerchoice  not in ["1","2","3"]:
        print("You must enter a 1,2,3.")
        return play_rps
    player = int(playerchoice)
    
    computerchoice = random.choice("123")
    computer = int(computerchoice)
    
    print("\nyou chose" + str(RPS(player)).replace("RPS." , " "))
    print("\npython chose" + str(RPS(computer)).replace("RPS.", " "))
    

    if player == 1 and computer == 1:
        print("Tie game!")
    elif player == 1 and computer == 2:
        print("python win!")
    elif player == 1 and computer == 3:
        print("you win!")
    elif player == 2 and computer == 1:
        print("you win!")
    elif player == 2 and computer == 2:
        print("Tie game!")
    elif player == 2 and computer == 3:
        print("python win!")
    elif player == 3 and computer == 1:
        print("python win!")
    elif player == 3 and computer == 2:
        print("you win!")
    elif player == 3 and computer == 3:
        print("Tie game!")
    else:
        print("you should enter number")

    print("\nplay again")
    while True:
        playagain = input("\nplay again?\nY for yes or \nQ to quit\n\n")
        if playagain.lower() not in ["y","q"]:
            continue
        else:
            break



    if playagain.lower() == "y":
        return play_rps()
    else:
        print("wowwww\n")
        print("thanks you for playing\n")
        sys.exit("bye")

play_rps()