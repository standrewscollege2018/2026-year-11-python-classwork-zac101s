'''This is a program to reccmmoend dosage'''

print("Welcome to the medicein")
#asking for age and weight
AGE = int(input("What is your age? "))

#Checking if they are between a certain age.
if AGE >= 1 and AGE <= 100:
    #Recomending tablet for child under 12
    if AGE <= 12:
     print("Your recmmoned dossage is two 500 milligram tablets" )
elif AGE >= 12: 
    #Recmmoding dossage for child over 12 based on weight
    WEIGHT = int(input("What is you weight? "))
    #Checking if the weight is vaild between 1 and 100kg
    if WEIGHT >=1 and WEIGHT <=100:
       REC = WEIGHT * 10
       print(f"Scence you are over 12 your recmonded dossage is {REC} milligrams")
    else:
       print("You have entered an invailid weight please enter a weight between 1 and 100kg")
else: 
   #The user has entered an invailed number so it will stop
   print("You have entered an invaild number, please enter a number between 1 - 100")
