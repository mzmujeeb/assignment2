#1. Write a python script to add comments and print “Learning Python” on screen.
 #Learning Python
print("Learning python")


#2. Write a python script to add multi line comments and print values of four variables, each in a new line. Variable contains any values.

'''
Learning
Python

'''
a=12
b=15
c=18
d=20
print(a)
print(b)
print(c)
print(d)

#3. Write a python script to print types of variables. Create 5 variables each of them containing different types of data. (like 35, True, “MySirG”,5.46, 3+4j, etc)

a=24
b= True
c= "MySirGi"
d= 5.24
e= 3+4j

print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))


#4. Write a python script to print the id of two variables containing the same integer values.

a= 24
b= 24
print(id(a))
print(id(b))

#5. Create four variables in a Python script and assign values of different data types to them. Write a Python script to print value, its type and id of each variable.

w=24
x= True
y= "MySirGi"
z= 5.24

print(w,type(w),id(w))
print(x,type(x),id(x))
print(y,type(y),id(y))
print(z,type(z),id(z))

#6. Write a python script to print all the keywords.

import keyword
print(keyword.kwlist)

#7. On Python shell use help() function and display the list of keywords.

#help()
'''
help> keywords

Here is a list of the Python keywords.  Enter any keyword to get more help.

False               class               from                or
None                continue            global              pass
True                def                 if                  raise
and                 del                 import              return
as                  elif                in                  try
assert              else                is                  while
async               except              lambda              with
await               finally             nonlocal            yield
break               for                 not

'''



#8. Create two Python files A0.py and A1.py. Create a variable in A1.py and assign somevalue to it. Write a python script to import A1 module in A 0 and print value of the variable created in A0.py

'''
A0
x=10

A1
import A1
print(A1.x)
'''

#9. Name the keywords, used as data in the Python script.
'''
False
None
True
'''

#10. Write a python script to display the current date and time. First create variables tostore date and time, then display date and time in proper format (like: 13-8-2022 and 9:00 PM)

from datetime import datetime
dt = datetime.today();
print(dt)

d1 = dt.strftime("%d-%m-%y and and %I:%M %p")
print(d1)



