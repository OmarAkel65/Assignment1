import sys
import random
from enum import Enum 


class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSOR = 3

playagain = True
while playagain :
# print(RPS(2))
# print(RPS.ROCK)
# print(["ROCK"])
# print(RPS.ROCK.value)
#  sys.exit()


   
    playerchoice = input("\nEnter... \n1 for Rock, \n2 for Paper, \n3 for Scissor: \n\n ")
    player = int(playerchoice)
    if player < 1 or player > 3:
        sys.exit("You must enter a 1,2,3.")
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
        
    playagain = input("\nplay again?\nY for yes or \nQ to quit\n\n")

    if playagain.lower() == "y":
        continue
    else:
        print("wowwww\n")
        print("thanks you for playing\n")
        playagain = False

sys.exit("bye")