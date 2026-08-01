# 10. Write a program to remove all occurrences of a given element in the list.

def remove(li,n):
    for i in range(len(li)):
        if li[i] != n:
            new.append(li[i])
        

li=[10,20,39,36,56,89]
n=int(input("Enter the element. you want to remove:"))
new=[]
remove(li,n)
print(new)