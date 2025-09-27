person = "dave"
coins = 3
print("\n" + person + " has " + str(coins) + " coins left ")

massage = "\n%s has %s coins left." %(person,coins)
print(massage)

massage = "\n{}  has  {}  coins left." .format(person,coins)
print(massage) 

massage = "\n{1}  has  {0}  coins left." .format(person,coins)
print(massage)

massage = "\n{person}  has  {coins}  coins left." .format(person = person,coins = coins)
print(massage)

massage = (f"\n {person} has {coins} left")
print(massage)

massage =  (f"\n {person.upper()} has {3*6} coins")
print(massage)
