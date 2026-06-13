#5. Write a program to enter P, T, R and calculate Compound Interest.

# Take input from user

P=float(input("Enter the Amount:"))
R=float(input("Enter the Rate:"))
T=float(input("Enter the Time:"))

# Perform operations

x=P*(1+R/100)**T
y=x-P

#Display Output

print("Compound Interest",y)
