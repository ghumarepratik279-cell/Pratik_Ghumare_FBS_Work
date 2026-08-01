# 6. Python Program to Find the Union of two Lists

def Union(li,li2,union):
    for i in li:
        if i not in union:
            union.append(i)

    for j in li2:
        if j not in union:
            union.append(j)

li=[39,23,44,53,45,32]
li2=[23,56,75,43,23,23]
union=[]
print("List 1:",li)
print("List 2:",li2)
Union(li,li2,union)
print("Union of list:",union)
