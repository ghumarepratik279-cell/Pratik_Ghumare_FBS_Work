# 1. Write a program to calculate area of rectangle

def area(l,w):
    area= l * w 
    return area

len=int(input("Enter the length:"))
wid=int(input("Enter the width:"))

res=area(len,wid)
print(f"Area of rectangle is {res} ")