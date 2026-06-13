###Numeric 
#1 int
x=10
print(type(x))

#2.float
x=3.14
print(type(x))

#3.complex
x=5+10j  #real + imaginary
print(type(x))

###Text
#1.str
x='Firstbit solution'
x="firstbit solution"

x='''this is first line.
this is second line.'''


x="""this is first line.
    this is second line."""

print(type(x))

###sequential 
#1. list
x=[10, 20, 30,]
print(type(x))


#2.tuple
x=(10, 20, 30)
print(type(x))


#3. range
x=range(1,10)
# print(type(x))
for i in range(10):
    print(i)



### Set Types
#1.set
x={10, 20, 30}
print(type(x))


#2 frozenset
x=frozenset({10, 20, 30})
print(type(x))

### Mapping
#1 Dictionary
x={1:'python',2:'java'}
print(type(x))


###Other
#1 Boolean
x=False
x=True
print(type(x))



#None Type
x=None
print(type(x))