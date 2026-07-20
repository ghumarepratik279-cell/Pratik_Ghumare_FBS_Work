# 3. Write a program to find sum of following series using functions :
    # a. 1+ 2 + 3 + 4+..... + n
    # b. 1!+ 2! + 3! + 4!+..... + n!
    # c. 1^1 + 2^2 + 3^3+ ...... n^n

def add(n):
    sum=0
    for i in range(n+1):
        sum+=i
    print(f"sum of 1 to {n} is {sum} ")


def fact(n):
    sum=0
    for i in range(1,n+1):
        f=1
        for j in range(1,i+1):
            f*=j
        sum=sum+f
    print(f"sum of 1 to {n} factorial is {sum}")

def power(n):
    sum=0
    for i in range(1,n+1):
        sum=i**i
    print(f"sum of 1 to {n} power is {sum}")

no=int(input("Enter the no:"))
add(no)
fact(no)
power(no)
