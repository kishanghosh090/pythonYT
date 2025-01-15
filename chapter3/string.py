name_one = "kishan rana ghosh"
name_two = 'kishan rana ghosh'
name_three = """kishan rana ghosh"""
for_skip_value = "0123456789"

another_name = name_two[0:6]
negetive_slice = name_two[-4: -1]
skip_value = for_skip_value[0:6:2]


# another_name_two = name_two.split(" ")

# print(another_name)
# print(negetive_slice)
# print(skip_value)


# ------------- functions in string------------------

print(len(name_one))
print(name_one.count("a"))
print(name_one.startswith("kishan"))
print(name_one.endswith("ghosh"))
print(name_one.capitalize())
print(name_one.upper())
print(name_one.lower())
print(name_one.replace("kishan rana", "akash"))
print(name_one.find("kishan"))