#4. Write a program to enter P, T, R and calculate simple Interest.

# Take input from user

P=float(input("Enter the Amount:"))
R=float(input("Enter the Rate:"))
T=float(input("Enter the Time:"))

# Perform operations

SI=P*R*T/100

#Display Output

print("Simple interest is::",SI)