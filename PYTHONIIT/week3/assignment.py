# name = input()
# nick = ''    # there is no space between the quotes
# space = ' ' # there is one space between the quotes
# first_char = True
# for char in name:
#     if first_char == True:
#         nick = nick + char
#         first_char = False
#     if char == space:
#         first_char = True
# print(nick)


# word = input()
# valid = True
# for i in range(len(word)):
#     char = word[i]
#     if i % 2 == 0 and char not in 'aeiou':
#         valid = False
# print(valid)

# n = 0
# for x in range(100):
#     for y in range(100):
#         if x != y:
#             print(f'{x},{y}')
#             n += 1

# print(n)

# n = 0
# x, y = 0, 0
# while x < 100:
#     y = 0
#     while y < 100:
#         if x != y:
#             print(f'{x},{y}')
#             n += 1
#         y += 1
#     x += 1

# print(n)


# print(0 % 2 == 0 ) 

# Note this prefix code is to verify that you are not using any for loops in this exercise. This won't affect any other functionality of the program.
with open(__file__) as f:
    content = f.read().split("# <eoi>")[2]
if "for " in content:
    print("You should not use for loop or the word for anywhere in this exercise")

# This is the first line of the exercise
task = input()
# <eoi>

if task == "sum_until_0":
    total = 0
    n = int(input())
    while n != 0: # the terminal condition
        total += n # add n to the total
        n = int(input()) # take the next n form the input
    print(total)

elif task == "total_price":
    total_price = 0
    while True: # repeat forever since we are breaking inside
        line = input()
        if line == "end": # The terminal condition
            break
        quantity, price = line.split() # split uses space by default
        quantity, price = int(quantity), int(price) # convert to ints
        total_price += quantity * price # accumulate the total price
    print(total_price)
elif task == "only_ed_or_ing":
    word = input()
    if word[-3:] == "ing":
        print(word[:-3] + "ly")
    else:
        print(word + "ing")

elif task == "reverse_sum_palindrome":
    total = 0
    while True:
        line = input()
        if line == "end":
            break
        total += int(line[::-1])
    print(total)

elif task == "double_string":
    word = input()
    print(word * 2)

elif task == "odd_char":
    word = input()
    print(word[1::2])

elif task == "only_even_squares":
    total = 0
    while True:
        line = input()
        if line == "end":
            break
        total += int(line) ** 2
    print(total)
elif task == "only_odd_lines":
    while True:
        line = input()
        if line == "end":
            break
        if int(line) % 2 == 1:
            print(line)
    
