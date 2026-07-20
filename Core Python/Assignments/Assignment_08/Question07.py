
def sum(n):
    t=n
    count=0
    while(t>0):
        d=t % 10
        t //= 10
        count += d
    print(f"No.of sum is: {count}")
num=int(input("Enter the number "))
sum(num)
