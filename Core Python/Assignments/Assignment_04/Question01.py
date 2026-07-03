# 1. WAP to print all even numbers until n.

n=int(input("Enter the no:"))
i=0
while i<n:
    if(i%2==0):
        print(i)
    i+=1