#1. Write a program to find sum of all elements of list

def sum(li):
    sum=0
    for i in range(len(li)):
        sum += li[i]
        
    print(sum)
    
li=[10,39,49,38,32,21]
sum(li)