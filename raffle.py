'''Raffle software to enter names and prxe value etc'''

import random 

# Welcoming the user

print("Welcome to the raffle program. ")
print()
print()


prizeask = True

while prizeask == True:
    prize = input("What is the prize being raffled? ")
    if prize == "":
        print("Enter a vaild name")
    else: prizeask = False
    

#Defining the while loop varible
askfornumber = True
asknames = True
entries = []


# While loop f
while askfornumber == True:
    try:
        value = input(f"What is the value of the {prize} (Do not enter $ sign) ")
        askfornumber = False
    except ValueError:
        print("Please enter a valid number ")

print("If you would like to finish entering name enter (stop)")
while asknames == True:
    names = input("Enter name of entrant: ")
    if names == "End":
        asknames == False
        
    elif names == "":
        print("Please enter a name")
    else:

        entries.append(names)

print(entries)
print(len(entries))
print(entries[random.randint(0,len(entries))])

