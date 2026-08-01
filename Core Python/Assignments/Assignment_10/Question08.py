# 8. Write a program to create a duplicate of an existing list. It should not point to
# same list.

def duplicate(li):
    for i in li:
        li2.append(i)

li=[20,34,21,34,56,76,76]
li2=[]

duplicate(li)
print(li)
print(id(li))
print(li2)
print(id(li2))

