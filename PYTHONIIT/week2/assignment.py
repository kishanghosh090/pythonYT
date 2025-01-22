# a = 3
# b=6
# c=90

# x, y, z = a, b, c
# # print(x, y, z)
# x = y = z
# # print(x, y, z)
# # print(x == y == z)
# # print(x == y == z == a)
# # print(x == y == z == b)
# # print(x == y == z == c)


# flag = True
# # if flag:
# #     print('works')

# bool_var =False
# x=10
# # if bool_var:
# #     x = x + 1
# #     bool_var = not bool_var
# #     if bool_var:
# #         x = x + 1
# #     else:
# #         x = x - 1
# # print(x)


# name = 'a'
# # print(int(name))


# x1 = input()
# x2 = input()
# y1 = input()
# y2 = input()
# y3 = input()
# z = input()

# # swap the values of `x1` and `x2`
# x = x1
# x1 = x2
# x2 = x
# # do a circular swap of `y1`, `y2` and `y3`  like y1 = y2, y2 = y3, y3 = y1 

# y = y1
# y1 = y2
# y2 = y3
# y3 = y

# # create a new variable `a` with the value of `z`
# a = z


# # A single quote ' and a double quote "
# output1 = 'A single quote \' and a double quote \"'

# # A forward slash / and a backward slash \
# output2 = 'A forward slash / and a backward slash \\'

# # Three single quotes ''' and three double quotes """
# output3 = 'Three single quotes \'\'\' and three double quotes \"\"\"'

# # Double forward slash // and Double backward slash \\
# output4 = 'Double forward slash // and Double backward slash \\\\'









# word = input()
# valid = False
# # both 'a' and 'z' are in lower case
# if 'a' <= word[0] <= 'z':
#     if word[0] == word[-1]:
#         valid = True
# print(valid)


# L=12

# # L is a positive integer that has already been defined at this stage
# word = input()
# space = ' ' # there is a single space
# if len(word) < L:
#     word = 'short' + space + word
# elif L <= len(word) < 2 * L:
#     word = 'medium' + space + word
# else:
#     word = 'long' + space + word
# print(word)

# #output1: short good
# #ouput2: long goodnessme

# # With just this data given to you, what is the value of L? (NAT)

num = input()
first, middle, last = int(num[0]), int(num[1]), int(num[2])
if first + last == middle:
    print('sandwich')
else:
    print('plain')