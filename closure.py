def parent_function(person): #def parent_function(person,coins):
    coins = 3

    def play_game():
        nonlocal coins
        coins -= 1

        if coins > 1:
            print("\n" + person + " has " + str(coins) + " coins left ")
        elif coins == 1 :
            print("\n" + person + " has " + str(coins) + " coins left ")
        else:
            print("\n" + person + " out of coins ")

    return play_game
    
tommy = parent_function("tommy")
tommy = parent_function("tommy")
jenny = parent_function("jenny")
tommy = parent_function("tommy")

tommy()
tommy()
jenny()
tommy()






            
    