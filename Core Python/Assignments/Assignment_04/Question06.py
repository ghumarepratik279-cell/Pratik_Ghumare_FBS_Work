#6. WAP to check if a given number is prime number or not.
n=int(input("Enter the no:"))
i=2
while(i<n-1):
    if(n%i==0):
        print("Not prime no.")
        break
    else:
        print("prime no.")
        break
    i+=1