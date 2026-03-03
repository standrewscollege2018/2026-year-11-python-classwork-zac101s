'''Basic rental car system for a local universty'''

cars = ["Suzuki Van (2)", "Toyota Corolla (4)", "Honda CRV (4)", "Suzuki Swift (4)", "Mitsubishi Airtrek (4)", "Nissian DC Ute (4)", "Toyota Previa (7) ", "Toyota Hi Ace 12", "Toyota Hi Ace (12)"]
names = []
bookloop = True 


print("Welcome to the Unversity vechiel rental system")
print()
print("The vehicles are: ")


for i in range(len(cars)):
    print(f"{i+1} {cars[i]}")

print()

while bookloop == True:
    try:
        book = int(input("Which car would you like to book? ")) 
    except ValueError:
        print("Please enter a vaild number")
    if 0 <= len(cars):
        print("It worked")
    else:
        print("It didnt work")
