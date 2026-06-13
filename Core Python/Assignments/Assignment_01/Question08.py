#8. Write a program to convert days into years, weeks and days.

#Take Input from user
days=int(input("Enter the Days:"))

#Perform Operations

year= days // 365
rdays=days % 365       #remaining days
week= rdays // 7       #convert into days
days=rdays % 7

#Display Output:

print(f"Year:{year} Remaing days:{rdays} Weeks:{week} days:{days}")
