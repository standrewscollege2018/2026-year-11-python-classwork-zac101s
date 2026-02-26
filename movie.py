'''Enter Movie names into a list'''

movienam = []

for i in range(3):
    movienam.append(input("Enter a movie name "))

for j in range(len(movienam)):
    print(f"{j+1} : {movienam[j]}")
 