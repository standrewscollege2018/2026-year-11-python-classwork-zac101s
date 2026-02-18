''' 
Bar codes usually consist of 13 digits eg 9425674564783. 
The first two digits give the country of origin, the next 5 the manufacturer, the next 5 give the product code. 
The last digit is used as a check digit.   
Write a program where the user inputs a bar code  
The program checks that it is 13 digits long : len() 
It then lists the country code, the manufacturer’s code, the product code and the check digit (you can Google some of these, or make them up)  
If the barcode does not have 13 digits, there should be an error message.
 '''

#Asking user for input and saving it as a varible
barcode = input("Please input your barcode ")

#Checking if the barcode is 13 chracters in length 
if len(barcode) == 13:
    #Then giving country code and manufacturer code
    print(f"Your barcode is {barcode}")
    print(f"Your country code {barcode[0:2]}")
    print(f"The manufacturer code is {barcode[2:7]}")
else:
    #Else enter a invailed number
    print("You entered an inavild number")