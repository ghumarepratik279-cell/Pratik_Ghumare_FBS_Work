#5. WAP to print Fibonacci series upto n.

n=int(input("Enter the no:"))
a=-1
b=1
i=0
while(i<n):
    c=a+b
    print(c)
    a=b
    b=c
    i+=1