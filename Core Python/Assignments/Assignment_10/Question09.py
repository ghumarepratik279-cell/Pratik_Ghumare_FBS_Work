# 9. Write a program of having n number of elements in the list and find out even and odd elements in that list and then create two separate lists which will have
# even elements and other will have odd elements.

def evenodd(li):
    for i in li:
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)

            

li=[10,30,23,23,45,43,22,13]
even=[]
odd=[]
evenodd(li)
print("Even list",even)
print("Odd list",odd)