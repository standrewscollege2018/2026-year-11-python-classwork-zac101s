'''1. Write a program which will ask the user for two numbers and will then give a message telling them the two numbers they entered, 
the larger of their two numbers, and the total of the two numbers.'''

#Asking user for the two numbers
num1 = int(input("Enter your first number: "))
num2 = int(input("Enter your secound number: "))

#checking which number is bigger or if invaild input will give error
if num1 < num2:
    print(f"{num2} is bigger then {num1}")
elif num1 > num2:
    print(f"{num1} is bigger then {num2}")
else:
    print("You have entered an invaild number")

#Adding the number togeather
print(f"The two number combined8 equal {num1 + num2}")