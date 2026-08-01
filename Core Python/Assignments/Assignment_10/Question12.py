# 12. Write a program to create three lists of numbers, their squares and cubes

def square_cube(li):
    for i in li:
        square.append(i**2)
        cube.append(i**3)


li=[20,19,30,45,43,22,11]
square=[]
cube=[]
square_cube(li)

print("original list:",li)
print("square list: ",square)
print("cube list; ",cube)