#6. Write a Program to input two angles from user and find third angle of the triangle.

# Take input from user

A1=int(input("Enter the 1st side:"))
A2=int(input("Enter the 2nd side:"))

# Perform operations

A3= 180 - (A1 + A2)

#Display Output

print("Third side of Triangle is::",A3)