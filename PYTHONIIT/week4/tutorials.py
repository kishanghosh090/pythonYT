#wormup with lists

# l = [1,2,3,4,5]
# l.append(1213)

# l.remove(3)

# x= []
# x.append(l)

# m = [1,2,3]

# x.append(m)

# # print(x)

# lists and sets------------------------------------

l = list(range(10))
l.append("kishan")

# print(5 in l)
x = list(range(10))
s = set(range(100))

import sys

# print(sys.getsizeof(l), sys.getsizeof(s))
# size of set is more than list
# print(l)

# print(s)


# Tuples-------------------------------------------
# l = [56,87,9,7,9]

# l.append(1987)

# t = (13,34,34234,213)
# print(t[0])

import string

# print(string.ascii_letters)

s = string.ascii_letters
# s = set(s)
s= tuple(s)
# print(s)

l = list(range(10))
t = tuple(range(10))

# print(l.__sizeof__(), t.__sizeof__())
# size of list is more than tuple


# More on lists


l1 = [1,2,3]
l2 = [4,5,6]
l3 = l1 + l2

# print(l3)

# l1 = [0,0,0,0,0,0]
l = [0]*6
l2 = [1,2,3] * 5
# print(l2)

l1= [1,2,3]
l2 = [1,2,3]
l3 = [1,3,2]
# print(l1 == l2)
# print(l1 == l3)


l1 = [1,2,3]

l2 = list(l1)
l3 = l1[:]
l4 = l1.copy()
l5 = l1

# print(l1 is l2)
# print(l1 is l3)
# print(l1 is l4)
# print(l1 is l5)


def append_to_list(l, x):
    l.append(x)
    return l


# l1 = [1,2,3]
# l2 = append_to_list(l1, 4)
# print(l1,l2)

# l = [1,2,3,4,0]

# l.insert(0,33)
# print(l)

# l.pop(0)
# print(l)

# l.sort(reverse=True)
# # l.sort(reverse=False)
# print(l)

# l.reverse()
# print(l)



# more on sets ------------------


s1 = {1,2,3,4,5} # does not allow duplicates values in sets

# print(s1)

a = {1,2,3}
b = {1,2,3,4,5,6}

# print(a.issubset(b))

c1 = a.union(b)
c2 = a.intersection(b)

# print(c1,c2)

# c3 = a.difference(b)
c3 = b.difference(a)
# print(c3)


# more on Tuples

# t1 = (1,2,3)

t1 = 1,2,3

# print(type(t1))

x,y,z = t1

# print(x,y,type(z))

t = ([1,2],['a','b'])

# print(t)
# t[0] = [3,4] # error as tuples are immutable 
t[0][0] = 3 # no error as list is mutable and we have list inside tuple

# print(t)


# functional programming

a = 10
b = 23

small = a if a < b else b

# print(f'small is {small}')

a = 5

# while a >= 0 :print(a, end=" "); a = a - 1

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newList = []

for fruit in fruits:
    if "a" in fruit:
        newList.append(fruit)
# print(newList)

newList = [fruit.capitalize() for fruit in fruits if "a" in fruit]

# print(newList)

# Inroduction to Functions

def add(a,b):
    return a + b


def disCount(cost,d):
    ans = cost - (cost * d / 100)
    print(ans)


# disCount(100,10)

# More examples of functions

def list_min(l):
    min = l[0]
    for i in range(1,len(l)):
        if l[i] < min:
            min = l[i]
    return min

# l = [1,2,3,4,5]
# print(list_min(l))

# Types of function argument

def add(a,b):
    return a + b

print(add(1,2))# positional argument
print(add(a=1,b=2))# keyword argument

def add(a,b=10,c=22):
    return a + b + c

print(add(1))

# types of functions-------
# 1. Built-in functions
# 2. library functions
# 3. user defined functions
# 4. class methods


