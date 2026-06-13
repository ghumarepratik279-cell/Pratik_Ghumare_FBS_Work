#Program Find the Quadratic Equation

#Take input from user
a=int(input("Enter A:"))
b=int(input("Enter B:"))
c=int(input("Enter C:"))

#Perform operations

d=b**2-4*a*c
r1=-b+(d**0.5)/(2*a)
r2=-b-(d**0.5)/(2*a)

#Display Output

print("Root 1 is::",r1)
print("Root 2 is::",r2)
