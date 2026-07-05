# for i in range(4):
#     for j in range(i,4):
#         print(" ",end=" ")
#     for j in range(1,i):
#         print(j,end=" ")
#     for j in range(i-1,1,-1):
#         print(j-1,end=" ")
#     print()


for i in range(1,5):
    for j in range(5-i):
        print("",end=" ")
    for j in range(1,i+1):
        if j==1 or j==i:
            print(1,end=" ")
        else:
            print(i-1,end=" ")
    print()