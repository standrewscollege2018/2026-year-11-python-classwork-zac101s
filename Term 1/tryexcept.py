''' Error catching to prevent invaild data types'''
get_num = True
while get_num == True:
    try:
        number = int(input("Enter a number"))
        get_num = False
    except ValueError:
        print("That is an invaild number")

print(f"You entered {number}")