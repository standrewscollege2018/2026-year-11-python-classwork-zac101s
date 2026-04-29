'''Demonstarting how lists work '''

# Lists are used to store multiple pieces of infomation
# We use square brackets to show it is a list.
names = ["Henry", "Spencer", "BMB", "Jesus"]

# Print the entire list
print(names)

print(names[3])

# Using negtive index counts backwards from the end
# -1 prints the last number
#print[-1]

# Can use len() to get the number of items in the list
length = len(names)

# Printing out the length of a specific item
print(len(names[3]))

# To change an item, just overwrite it by setting a new value for that position

# You can insert items into a particular postion in a list 
names.insert(1,"your mum")
print(names)

#The most common method of adding items is to add them at the end using append()
names.append("Mike")
print(names)

# When displaying all items from a list it is best to use a loop rather than printing the whole 
for name in names:
    print(name)

for i in range(len(names)):
    print(f"{i+1} {names[i]}")
