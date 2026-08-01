# 4. Python Program to Find the Second Largest Number in a List Using 

def BubbleSort(li):
    size = len(li)
    for i in range(1,size):
        for j in range(0,size-i):
            if li[j] > li[j+1]:
                li[j],li[j+1] = li[j+1],li[j]

li=[40,20,70,50,34,55]
print("Before sort",li)
BubbleSort(li)
print("After sort ",li)
print("second largest element is:",li[-2])