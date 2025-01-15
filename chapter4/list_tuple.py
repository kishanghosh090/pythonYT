# lists are mutable and it can be changed

chai = ["lemon tea", "alychi tea","zinzer tea", "black tea"]
print(chai)
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
print(L1)