#9. Write a program to check if entered number is a palindrome or not.

def ispallindrome(n):
    t=n
    rev=0
    while(t>0):
        d=t%10
        t//=10
        rev=rev*10+d
    if(n==rev):
        return True
    else:
        return False

num=int(input("Enter the no:"))
pal=ispallindrome(num)

if pal==True:
    print("No is pallindrome")
else:
    print("No is not pallindrome")