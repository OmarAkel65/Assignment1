name = "Dave" #global scope

def greeting(name):
    color = "blue"  #local scope
    print(color)
    print(name)

greeting("john")

def another():
    greeting("Dave")
another()

def another():
    color = "blue"
    def greeting(name):
        print(color)
        print(name)

    greeting("dave")

another()

name = "dave"
count = 1

def another():
    color = "blue"
    global count
    count +=1
    print(count)
    def greeting(name):
        nonlocal color
        color = "red"
        print(color)
        print(name)
    greeting("dave")