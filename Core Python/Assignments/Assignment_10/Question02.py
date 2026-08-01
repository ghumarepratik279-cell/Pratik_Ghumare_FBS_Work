#2. Write a program to find maximum and minimum element in a list.

def minmax(li):
    max=li[0]
    min=li[0]
    for i in range(len(li)):
        if  li[i] > max :
            max=li[i]
        if  li[i] < min :
            min=li[i]
    print(f"minimum element is {min}")
    print(f"maximum element is {max}")

li=[23,43,25,90,10,35]
minmax(li)
#  print(f"maximum element is {li[i]}")