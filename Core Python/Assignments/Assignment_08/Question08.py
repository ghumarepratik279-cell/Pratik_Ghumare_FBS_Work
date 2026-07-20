

def reverse(n):
    t=n
    rev=0
    while(t>0):
        d=t%10
        t//=10
        rev=rev*10+d
    return rev
num=int(input("Enter the no"))
res=reverse(num)
print("Reverse no is:",res)