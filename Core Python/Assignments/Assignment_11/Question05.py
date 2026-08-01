# 5. Python Program to Sort a List According to the Length of the Elements within the list.

def lensort(li):
    li.sort(key=len)

li = ["Dog", "Camel", "Elephant", "Tiger", "cat"]
print("Oriinal List :", li)
lensort(li)
print("Sorted List :",li)