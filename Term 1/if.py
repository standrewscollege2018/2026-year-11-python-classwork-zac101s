'''Demonstatrting how a conditional statement (if/else) works It asks the user for a password and the checks if it is correct'''

Saved_password = "12345678"
Saved_username = "zac"
#Asks for password and username, then stores in a variable
username = input("What is your user name ")
Passwords = input("What is you password ")

#Checks if username and password is correct and if not correct denies entry
if username == Saved_username and Passwords == Saved_password:
    print("Access Granted")
else:
    print("You don't have access")

