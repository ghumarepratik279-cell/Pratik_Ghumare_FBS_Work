for i in range(1,6):
    for j in range(6-i):
        print(" ",end=" ")
    
    n=i
    for i in range(1,i+1):
        print(n,end=" ")
        n+=1

    n-=2
    for j in range(i-1):
        print(n,end=" ")
        n-=1
    print()
