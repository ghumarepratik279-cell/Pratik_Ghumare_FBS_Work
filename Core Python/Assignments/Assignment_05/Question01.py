# 1. Write a program to prompt user to enter userid and password. If Id and password is incorrect give him chance to re-enter the credentials. Let him try 3
# times. After that program to terminate.

id="pratikg"
pas=231
n=3
for i in range(0,n):
    print(f"You have {n} chance to enter correct id & password")
    user_id=input("Enter the User_id:")
    passw=int(input("Enter the the Password:"))
    if(id==user_id and pas==passw):
        print("Login succesfully!..")
    else:
        print("Enter the correct credential!")
    n-=1