f = open("chai.txt", "r")
# print(f.read(10))

# print(f.readline())
# print(f.readline())
# print(f.readline())
# print(f.readline())

# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__()) # StopIteration: error occurs


# for line in open("chai.txt"):
    # print(line, end="") # end="" is used to remove the new line character


# myList = [1, 2, 3, 4, 5] 
# myIter = iter(myList)
# print(next(myIter))
# print(next(myIter))
# print(next(myIter))
# print(next(myIter))
# print(next(myIter))
# print(next(myIter)) # StopIteration: error occurs   


f = open("chai.txt", "r")
# iterF = iter(f)

# print(f is iter(f)) # False

# print(iter(f) is f.__iter__()) # True

myNewList = [1, 2, 3, 4, 5]

# print(myNewList.__iter__() is myNewList) # True


d = {'a': 1, 'b': 2, 'c': 3}

for key in d.keys():
    print(key, d[key])

i = iter(d)

print(next(i))
print(next(i))
print(next(i))
# print(next(i)) # StopIteration: error occurs

print(range(5))