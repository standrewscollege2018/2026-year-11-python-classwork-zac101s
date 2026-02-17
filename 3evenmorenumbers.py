'''Write a program to ask the user for numbers between 50 and 100 and to keep adding them to the total. 
The program should stop adding and print out the grand total once the total is bigger than 200. '''

#Setting varibles for the adding and the while loop
val_input = True
add = 0

#starting the while loop
while val_input == True:
    #Asking user to enter number betwwen 50 and 100 until the numbers added is bigger than 200
    num = int(input("please enter a number between 50 and 100: "))
    #Checking if the user entered a number between 50 and 100
    if num <= 100 and num >= 50:
        add += num
        print(add)
    else:
        print("Please print a number between 50 and 100")
    if add >= 200:
        print(f"Your {add} is bigger than 200")
        val_input = False