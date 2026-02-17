'''Numebr guessing game'''

#defing the boolen to start as true
#Inporting the random package
import random

#Settting varibles
NUMBER = random.randint(1,100)
ASK_GUESS = True
times_taken = 0

while ASK_GUESS == True:
    #Asking for number input
    guess = int(input("Whats your number guess bettween 1 and 100 or 101 to exit: "))

    #Added exiting
    if guess == 101:
      print("Exiting")
      ASK_GUESS = False
      break

    #Cheking if number is bettween 1 and 100
    if guess >=1 and guess <=100:
        if guess > NUMBER:
         #Checking if number is lower than chosen number
         print("Number is to high")
         times_taken += 1
        elif guess < NUMBER:
         #Checking if number is higher than choosen number
         print("Number is to low")
         times_taken += 1
        elif guess == NUMBER:
         #Checking if the number is that same with choosn number which is right
         print("you have found the right number. Yay!")
         print(f"It has taken you {times_taken} times to finish")
         ASK_GUESS == False
    else:
      #Else if the number isnt bettween 1 and 100 it restarts you
      print("Invaild number try again")
