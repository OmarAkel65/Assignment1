import sys
import random
from enum import Enum 

def rps():
    game_count = 0
    player_wins = 0
    python_wins = 0 

    def play_rps():
        nonlocal player_wins
        nonlocal python_wins

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
        
        def decide_winner(player,computer):
            nonlocal player_wins
            nonlocal python_wins
            if player == 1 and computer == 1:
                return "Tie game!"
            elif player == 1 and computer == 2:
                python_wins += 1
                "python win!"
            elif player == 1 and computer == 3:
                player_wins += 1
                "you win!"
            elif player == 2 and computer == 1:
                player_wins += 1
                "you win!"
            elif player == 2 and computer == 2:
                "Tie game!"
            elif player == 2 and computer == 3:
                python_wins += 1
                "python win!"
            elif player == 3 and computer == 1:
                python_wins += 1
                "python win!"
            elif player == 3 and computer == 2:
                player_wins += 1
                "you win!"
            elif player == 3 and computer == 3:
                "Tie game!"
            else:
                "you should enter number"

        game_result = decide_winner(player,computer)
        print(game_result)

        nonlocal game_count
        game_count += 1
        print("\nGame count:" + str(game_count))
        print("\nplayerwins:" + str(player_wins))
        print("\npythonwins:" + str(python_wins))



        print("\nplay again?")
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
    return play_rps

play = rps()
play()