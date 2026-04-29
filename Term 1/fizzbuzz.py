'''This is a fizz buzz game'''

for number in range(1,31):
    if number % 3 == 0 and number % 5 == 0: 
        print("FizzBuzz")
    elif number % 3 == 0:
        print("fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print("Number")
        