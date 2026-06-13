gender=input("enter the gender")
age=int(input("enter the age"))

if(gender=='female'):
    if(age>=18):
        print("Eligible for marrige")
    else:
        print("Not eligible for marrige")
else:
    if(age>=21):
        print("Eligible for marrige")
    else:
        print("Not eligible for marrige")

