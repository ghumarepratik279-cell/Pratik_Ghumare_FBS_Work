# 3. Accept no. of passengers from user and per ticket cost. Then accept age of each
    # passenger and then calculate total amount to ticket to travel for all of them based on
    # following condition :
    # a. Children below 12 = 30% discount
    # b. Senior citizen (above 59) = 50% discount
    # c. Others need to pay full.

n=int(input("Enter the no of passanger:"))
t=int(input("Enter the total cost of 1 ticket:"))
ch=0
sc=0
full=0

for i in range(1,n+1):
    age=int(input("Enter the age of {i} no passanger "))
    if(age<=12):
        ch+=70*t/100
    elif(age>=59):
        sc=50*t/100
    else:
        full+=t

print("Total price to travel is:",ch+sc+full)