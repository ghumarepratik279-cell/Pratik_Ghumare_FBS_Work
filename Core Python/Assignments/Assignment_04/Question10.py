#10. WAP to check if given number is Perfect Number.
n=int(input("Enter the no:"))
sum=0
for i in range(1,n):
    if(n%i==0):
        sum=sum+i
    
if(sum==n):
    print("Number is perfect.")
else:
    print("Number is not perfect")
    