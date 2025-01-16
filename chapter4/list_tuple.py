# lists are mutable and it can be changed

chai = ["lemon tea", "alychi tea","zinzer tea", "black tea"]
# print(chai)
# print(type(chai))
# print(chai.copy())

chai[3] = "green tea"

# print(chai)


L1 = [1,2,3,45,54,1,34,545]
# L1.sort()
# L1.reverse()
# L1.append(12)

L1.insert(2, "kishan")
L1.pop(2)# removes the element at index 2 and returns it
L1.remove(45) # removes a perticuler value

# print(L1)


# ***  tuples are immutable ******

t1 = (1,2,1,3,46,76,"kishan","coffee")
# t1[2] = 4 # throws error as touples are immutable in python

# print(t1.count(1))

 # tuple methods------
print(t1.index("kishan"))
print(t1.__add__((1,2,3)),t1)