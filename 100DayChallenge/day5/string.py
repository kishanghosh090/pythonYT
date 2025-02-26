name = "alychi tea"
# string is immutable which means you can't change the value of a string
# name[0] = "A" # this will raise an error
name = "Alychi Tea" # this is the correct way to change the value of a string as 'Alychi Tea' is a new string which is assigned into antother memory location

# string concatenation
name = "Alychi" + " " + "Tea"
# print(name)

# multiline string

name = """Alychi
Tea"""
# print(name)

# sliceing in string
name = "Alychi Tea"
# print(name[0:6]) # Alychi
# print(name[7:]) # Tea

# print(name[-1: -4]) 

# print(name[-10:-1]) # Alychi Te
# print(name[-10:0]) #empty string
print(name[-10:])