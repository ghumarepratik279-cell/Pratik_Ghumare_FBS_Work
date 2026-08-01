# 13 . Write a program to print list after removing even numbers.

def removeEven(li,new):
    for i in range(len(li)):
        if li[i] % 2 != 0:
            new.append(li[i])


li=[1,2,3,4,5,6,7,8,9]
new=[]
removeEven(li,new)
print("Original list",li)
print("list After removing Even no.",new)