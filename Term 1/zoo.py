''' Checking if a person at the zoo has to pay child prices'''

#> = Greater thann
#< = Less than

#saving child age
#Must be in caps for constants
CHILD_AGE = 13

#asking for the age of the person entring
print("Welcome to the ZOO!")
AGE = int(input("How old are you?"))

if AGE < CHILD_AGE:
    print("You pay the child price")
else:
    print("You pay full price :)")


