# 2. Write a program to calculate area of circle

def circle(r):
    pi=3.14
    return pi*r**2

radius=int(input("Enter the radius:"))
res=circle(radius)
print(f"Area of circle is {res}")