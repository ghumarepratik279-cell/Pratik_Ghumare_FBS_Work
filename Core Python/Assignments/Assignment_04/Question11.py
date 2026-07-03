#11. WAP to check if given number Strong Number.
# 145= 1! + 4! + 5!
n= int(input("Enter the no:"))
temp=n
sum=0
while(temp>0):
    d=temp % 10
    temp //= 10
    fact=1

    for i in range(1,d+1):
        fact=fact*i

    sum+=fact
if(sum==n):
    print("Strong no.")
else:print("Not Strong no.")