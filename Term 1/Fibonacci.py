'''
The Fibonacci series is a series of numbers where each successive term is found by adding the two terms before it. 
The series starts 1, 1, 2, 3, 5, 8 etc.  
Write a program that will ask the user how many terms they wish to see, and then outputs the series for that many terms.
'''

#Setting the varibles 
a = 1
b = 0

#Asking the user for how many terms you would like to print
term = int(input("How many terms would you like to print "))

for i in range(0,term):
    a = b+a
    print(a)
    b = a+b
    print(b)
