
# lists are mutable and it can be changed
d= {} # empty dictionary
marks = {
    16: 100,
    "akash": 90,
    "rana": 80,
    "teas": ["alychi tea","zinzer tea", "black tea"]
}

# dict methods 

# print(marks.items())
# print(marks.keys())
# print(marks.values())

# print(marks.get("akash"))
# print(marks["akasha"])

# marks.update({"kishan":100})

# print(marks)


# --------------sets ------------------

empty_set = set() # empty set

sets = {12,34,54,656,676}

sets.add(12)
sets.remove(34)
# print(sets)
# print(len(sets))

s1 = {1,2,3,4,5}
s2 = {3,4,5,6,7}
s3 = s1.union(s2)
s4 = s1.intersection(s2)
s5 = s1.difference(s2)
s6 = s2.difference(s1)

print(s3)
print(s4)
