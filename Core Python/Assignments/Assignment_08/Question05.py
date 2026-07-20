# # 5. Sum of all prime numbers between 1 to n

def prime(n):
    sum=0
    for i in range(2,n):
        for j in range(2,i):
            if(i%j ==0):
                break
        else:
            print(i)

no=int(input("Enter the any no:")) 
prime(no)           

# n=int(input("Enter the no:"))
# def prime(n):
#     for i in range(2,n):
#         for j in range(2,i-1):
#             if(i%j==0):
#                 break
#         else:
#             print(i)
# num=int(input("Enter the no:"))
# prime(num)