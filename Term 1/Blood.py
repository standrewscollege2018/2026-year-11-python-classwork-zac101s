'''program to check is some one is enlagable for blood donation'''

#Min age and Weight
MIN_AGE = 16
MIN_WEIGHT = 50

#Asking for weifght and age 
age = int(input("What is your age "))
weight = int(input("What is your weight"))

if weight < MIN_WEIGHT or age < MIN_AGE:
    print("Sorry you cannot donate blood")
else:
    print("You can donate! Thank you for your support")