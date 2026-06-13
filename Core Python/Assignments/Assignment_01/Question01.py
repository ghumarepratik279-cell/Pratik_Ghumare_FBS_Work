#1. Write a program to calculate the percentage of student based on marks of any 5 subjects.

# Take input from user

S1=int(input("Enter the marks Sub 1:"))
S2=int(input("Enter the marks Sub 2:"))
S3=int(input("Enter the marks Sub 3:"))
S4=int(input("Enter the marks Sub 4:"))
S5=int(input("Enter the marks Sub 5:"))

# Perform operations

Total=S1+S2+S3+S4+S5
percentage=(Total/500)*100

#Display Output

print("total marks of student is",Total)
print("percentage of student is",percentage)
