# 4. WAP to print Armstrong number within a given range

start=int(input("Enter the starting no:"))
stop=int(input("Enter the stoping no:"))
for i in range(start,stop+1):
    c=0
    s=0
    t=i
    while(t>0):
        d=t%10
        t=t//10
        c+=1
    t=i
    while(t>0):
        d=t%10
        t=t//10
        s+=d**c
    if(s==i):
        print(i)