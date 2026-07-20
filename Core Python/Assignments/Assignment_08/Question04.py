#4. Sum of all odd numbers between 1 to n

def odd(n):
    sum=0
    for i in range(n):
        if(i%2!=0):
            print(i)
            sum=sum+i
    print(sum)
no=int(input("Enter the no:"))
odd(no)
