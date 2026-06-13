#Find the sum of three digit no.

#Take input from user
num=int(input("Enter three digits no:"))

#perform operations
d1=num % 10
num=num // 10

d2=num % 10
num=num // 10

d3=num % 10
num=num // 10

sum=d1+d2+d3

#display output
print("Sum of three digits is:",sum)