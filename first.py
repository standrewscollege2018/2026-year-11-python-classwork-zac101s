'''This program demonstatres print(), data types, variables, inputs and f-strings'''
# print() is a function that outputs whatever is inside the brackets
# numbers can be included directly in the brackets
print(123)

# when printing text, it must be in speecjmarks which turns it into a string
print("Hello")
# There are lots of diffrent data types:
# integers, decimals (floating point numbers)
# text (string), boolean

# We use varibles to store infomation
# variables must be all lower case
# if you want mulitple words in the varible name, use underscore
name = "Charlie"
firt_name = "mike"
last_name = "smith"
age = "67"

print(f"This person name is name is {name} {last_name} and she is {age} years old and likes to be called {firt_name}")

# Getting infomation from the user and then displaying it.
otname = input("What you name? ")

print(f"Hello {otname}!")

childage= input("how old are you? ")

print(f"You are {otname}, and you are {childage} years old")


