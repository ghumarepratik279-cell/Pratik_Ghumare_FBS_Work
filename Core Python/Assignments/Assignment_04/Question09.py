#9. WAP to print all numbers in a range divisible by a given number.
n=int(input("Enter the no:"))
m=int(input("Enter the Given no:"))
for i in range(1,n):
    if(i%m==0):
        print(i)