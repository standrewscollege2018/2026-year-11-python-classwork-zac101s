'''Multiple lists'''


import time 

# Setting the lists
name = ["Henry", "Cameron", "Harisung", "Niko"] 
driver = ["No Licence", "No Licence", "Learners", "Restricted"]
license = (["learners", "restricted", "full", "no licence"])

# Setting the while loop varible and setting titles
status = True 
print("Driver Licence Records")
print(40 * "=")
while status == True:

    # Printing the lists in an ordered format
    for i in range (len(name)):
        print(f"{i+1} {name[i]:>10} {driver[i]}")
    
    #First try and except to catch any vaild input errors
    try:
       update = int(input("Select student to update (0 to quit) "))
       if update == 0:
            status == False 
            break
       # Main code to update the license status of the students and error catching for invaild inputs
       elif update > 0 and update <= len(name):
            new = input("Enter New Status(Learners, Restricted, Full, No Licence) ")
            new_low = new.lower()
            if new_low in license:
                driver[update - 1] = new_low
                if driver[update - 1] == new_low:
                    print(f"{name[update - 1]} is already set to ({new_low})")
                else:
                    driver[update - 1] = new_low
                    for i in range (len(name)):
                        print(f"{i+1} {name[i]:>10} {driver[i]}")
            else:
                print("Invalid license type.")

                #time.sleep(2)
            

       else:
            print(f"Enter a vaild input between 1 and {len(name)}")
            #time.sleep(2)
    
    except ValueError:
        #ime.sleep(2)
        print("Enter a vaild input")


