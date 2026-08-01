# 2. Python Program to Merge Two Lists and Sort it

def merge_sort(li,li2):
    merge=li+li2
    merge.sort()
    return merge

li=[20,10,30,42,13,65]
li2=[34,24,65,32,45,32]
m=[]
merge=merge_sort(li,li2)
print("list 1:",li)
print("list 2:",li2)
print("Merge and sort list:",merge)

