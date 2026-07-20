#11. WAP to check if a given number is Armstrong number or not. For each task create separate functions.

def power(n):
    t=n
    i=0
    while(t>0):
        d=t%10
        t//=10
        i+=1
    return i

def armstrong(n,power):
    t=n
    sum=0
    while(t>0):
        d=t%10
        t//=10
        sum+=d**power
    return sum
n=int(input("Enter the no:"))
i=power(n)
res=armstrong(n,i)
if(res==n):
    print("No is Armstrong.")
else:
    print("No is not Armstrong.")