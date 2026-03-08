'''Rental car system 2 based of the forst one.'''

#Setting the lists for the cars, renter name, and if it is avalible
cars = ["Suzuki Van (2)", "Toyota Corolla (4)", "Honda CRV (4)", "Suzuki Swift (4)", "Mitsubishi Airtrek (4)", "Nissian DC Ute (4)", "Toyota Previa (7) ", "Toyota Hi Ace 12", "Toyota Hi Ace (12)"]
names = ["", "", "", "", "", "", "", "", "", ]
available = [True, True, True, True, True, True, True, True, True, ]

booking = True 
selection = True

print("Welcome to the Unversity vechiel rental system")
print()
print('If you would like to exit please enter 0')
print("The vehicles are: ")
print()


while selection == True:
    for i in range(len(cars)):
        if available[i] == True:
            status = ""
        else:
            status = "- (Unavailable)"
        print(f"{i+1} {cars[i]} {status}")
    try:
        book = int(input("Please enter a car you would like to book "))
        if book == 0:
            print("Exiting booking system")
            booking = False
            selection = False
            
        elif book <= len(cars) and book >= 1:
            if available[book -1] == False:
                print("Sorry this car is already booked")
            else:
                name = input("What is your name you would book this car under? ")
                if name.isspace():
                    print("This only has spaces try again")
                else:
                    print(f"Thank you {name} you have booked {cars[book - 1]}")
                    available.insert(book - 1, False)   
                    names.insert(book - 1, name)
        else:
            print(f"Please enter a number from 1 to {len(cars)}")
        
    except ValueError:
        print("Please enter a valid number")

         
        