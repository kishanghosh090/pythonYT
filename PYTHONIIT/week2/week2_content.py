# -------------------------- lec 3 ----------------
a = 10 
# print(type(a))
a = a/2
# print(type(a))

#------------------------- lec 4 ----------------

# and = 5 # error as and is a keyword
# 123abc = 45 # error as 123abc is not a valid variable name varibale not allowed to start with numbers

_name = "kishan" # valid variable name

x,y = 10,20
# print(x,y)

a=b=c=10
# print(a,b,c)

x,y = 10,20
x,y = y,x
# print(x,y)

del x # delete the variable explicitly
# print(x)

# print('it\'s good day to learn python') # escape sequence character

x =5

# print(1<x<10)
# print(x<10<x*10<100)
# print(10>x<=5)
# print(5==x>4)


#------------------------lec 5 ----------------
# print('My name is kishan \t i am from malda')

x='this is a string'
y="i love to write code in python"
z='''
this is a multi
line string''' 

# ------------------ lec 6 ----------------
X = "kIsHaN Rana GHoSh"

# print(X.upper())
# print(X.lower())

# print(X.capitalize()) # convert to captital 1st char of 1st word and small all next chars
# print(X.title())
# print(X.swapcase())

# print(X.islower())
# print(X.isupper())
# print(X.istitle())

X = '123#'

# print(X.isdigit())
# print(X.isalpha())
# print(X.isalnum())

X = "----python----"

# print(X.strip('-')) 
# print(X.lstrip('-'))
# print(X.rstrip('-'))

X = "Pythonnnn"

# print(X.startswith('p'))
# print(X.endswith('n'))

# print(X.count('p'))
# print(X.find('n'))
# print(X.index('n'))
# print(X.replace('p','q'))

# ------------------ lec 7 ----------------
alpha = "abcdefghijklmnopqrstuvwxyz"

name = "kishan"
i = 10
newName = ''
# print(i%26)

for i in range(0,len(name)-1):
    newName = newName + alpha[(alpha.index(name[i])+1)%26]

# print(newName)    


# ---------------------- lec 8 ----------------

# --------------------- lec 9 ----------------

# --------------------- lec 10 ----------------
import math

# print(math.pi)
# print(math.sin(90))

import random
# print(random.randint(1,10))

# --------------------- lec 11 ----------------

# from calendar import *

# print(calendar(2025))

from calendar import month
# print(month(2025,2))



#################### second time practice ####################

x = "kIsHaN Rana GHoSh"
# print(x)
# print(x.lower())
# print(x.upper())
# print(x.capitalize())
# print(x.title())
# # print(x.swapcase())

# print(x.islower())
# print(x.isupper())
# print(x.istitle())
# print(x.isdigit())
# print(x.isalpha())
# print(x.isalnum())

y = "----python----"
# print(y.strip('-'))
# print(y.lstrip('-'))
# print(y.rstrip('-'))

z = "Python string"

# print(z.startswith('p'))
# print(z.endswith('n'))

# print(z.count('t'))
# print(z.index('t'))
# print(z.find('t')) 
# print(z.replace('t','q'))


alpha = "abcdefghijklmnopqrstuvwxyz"

name = "kishan" # ljsibo
i = 10
newName = ''
# print(i%26)

# for i in range(0,len(name)):
#     print(alpha[(((alpha.index(name[i]))+2)%26)])



# for i in range(0,len(name)*10):
#     print(i%26)

import random
# print(random.random())
# print(random.randint(1,10))

from calendar import *
print(calendar(2025))