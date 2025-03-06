# f = open('text.txt', 'w')

# f = open('text.txt', 'a')

# f.write("\nkishan\n")
# f.write("Rana\n")
# f.write("Ghosh\n")


f = open('text.txt', 'r')

# print(f.read(10))

# print(f.readline())

print(f.seek(1))
print(f.read())