for i in range(1, 21, 2):
    print(i, end=' ')
print()

#A

for i in range(0,101,10):
    print(i, end=" ")
print()

#B

for i in range(20,0,-1):
    print(i, end=" ")
print()

#c. print a number of stars.
star_count = int(input("Enter a number:"))
for i in range (star_count):
    print("*", end="")
print()

#d. print lines of increasing stars.
number_of_stars = int(input("Enter a number:"))
for i in range (1,number_of_stars+1):
    print("*" * i)



