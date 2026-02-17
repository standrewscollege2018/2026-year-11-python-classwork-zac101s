'''Write a program that asks the user for a number. 
It then asks the user for a second number that is greater than the first. 
If it is not, the program should continue asking the user for a greater number until they successfully enter it.
Then the program prints out the two numbers.'''

#asking the user for number 1
num1 = int(input("Please enter your first number "))

#setting the varible for the while loop to true
vaild_input = True

#Checking if the number is greater then the first number entered and then printing the two number
while vaild_input == True:
    num2 = int(input("Please enter your secound number that is greater than the frist number "))
    if num2 > num1:
        print(f"Number 1 is {num1}")
        print(f"Number 2 is {num2}")
        vaild_input = False
    #Else it will keep asking for the input
    else:
        print("The number isnt greater, please try again")
        
