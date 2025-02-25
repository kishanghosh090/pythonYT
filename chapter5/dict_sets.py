
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

# print(s3)
# print(s4)

word1 = "Wingardium" # str
word2 = "Leviyosa" # str
word3 = "Silver" # str
sentence = "Learning python is fun"
n1 = 6 # int
n2 = 4 # int
# <eoi>

output1 = word1 + " " + word2 # str: join word1 and word2 with space in between
output2 = word1[:4] + "-" + word2[-4:]  # str: join first four letters of word1 and last four letters of word 2 with a hyphen "-" in between
output3 = word3 + " " + str(n1) # str: join the word3 and n1 with a space in between
print(output1)