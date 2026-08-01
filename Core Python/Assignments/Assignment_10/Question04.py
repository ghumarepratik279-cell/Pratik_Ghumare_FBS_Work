# 4. Write a program to reverse the list.

def reverse(li):
    for i in range(len(li)-1,-1,-1):
        rev.append(li[i])

li=[10,20,30,40,50,60,70]
print("original list",li)
rev=[]
reverse(li)
print("reverse list ",rev)
