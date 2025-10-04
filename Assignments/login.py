username = "admin"
password = "1234"


for attempt in range (3):

    username = input("Enter Your name: ")
    password = input("Enter your password: ")
    
    if username == "admin" and  password == "1234":
        print(f"welcome {username}")
        break
    else:
        if attempt <3 :
            print(f"you have {3 - attempt} attempts left")

else:
    print("Account Locked")
