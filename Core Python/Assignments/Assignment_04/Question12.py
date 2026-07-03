# 12. Write a program to check if given number is Armstrong number or not.
# (Hint : 153 = 1*1*1 + 5*5*5 + 3*3*3 , 1634 = 1*1*1*1 + 6*6*6*6 + 3*3*3*3 + 4*4*4*4)

n=int(input("Enter the no:"))
t=n
i=0
sum=0
while(t>0):
    d= t % 10
    t = t //  10 
    i+=1
# print(i)
t=n
while(t>0):
    d= t % 10
    t = t // 10
    sum+=d**i
if(n==sum):
    print("Armstrong no.")
else:
    print("Not Armstrong no.")