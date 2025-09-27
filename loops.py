sorted
names = ["Dave" ,"Sara" ,"John"] 
for x in names:
    print(x)

for x in "Mississippi":
    print(x)

for x in names:
    if x == "Sara":
        break
    print(x)

for x in names:
    if x == "Sara":
        continue
    print(x)

for x in range(5):
    print(x)

for x in range (2,4):
    print(x)

for x in range(5,100,5):
    print(x)
else:
    print("Glad that\'s over")

names = ["Dave" , "Sara" ,"john"]
actions = ["codes", "eats" , "sleeps"]

        
for action in actions:
    for name in names:
        print(name + " " + action + ".")

for name in names:
    for action in actions:
        print(name + " " + action + ".")


    