# 5. Accept a number from user and check if this element is present in the list or
# not. Also tell how many times it is present in the list.

def element(li,ele):
    if ele in li:
        print("Element is present")
        print("count:",li.count(ele))
    else:
        print("Element is not present")

li=[10,20,30,43,53,20,99]
search=int(input("Enter the element:"))
element(li,search)