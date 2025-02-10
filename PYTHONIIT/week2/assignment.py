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

# num = input()
# first, middle, last = int(num[0]), int(num[1]), int(num[2])
# if first + last == middle:
#     print('sandwich')
# else:
#     print('plain')



# Three single quotes ''' and three double quotes """
# output3 = 'Three single quotes \'\'\' and three double quotes """'
# # print(output3)

# # Double forward slash // and Double backward slash \\
# output4 = 'Double forward slash // and Double backward slash \\\\'
# print(output4)


# # part 1 - If pattern
# word = "glow" # str
# continuous_tense = True # bool

# # part 2
# age = 5 # int
# is_member = True # bool

# # part 3

# color_code = "R" # str: valid values are R-red, G-green and B-blue

# time = "02 PM" # str, format:[2-digit hour][space][AM or PM]
# # Morning (6 AM - 12 PM) (including the start and excluding the end)
# # Afternoon (12 PM - 6 PM) 
# # Evening (6 PM - 12 AM)
# # Night (12 AM - 6 AM)

# # <eoi>

# # part 1 - basic if

# new_word = word # donot remove this line

# # remove the "ing" suffix from `new_word` if it is there
# if (new_word[-3:] == "ing"):
#     new_word = new_word[:-3]

# print(new_word)

# # add the suffix "ing" to `new_word` if `continuous_tense` is True
# # write the whole if else block here

# # part 2 - If else pattern

# # age_group:str should be "Adult" or "Child" based on the age. assume age greater than or equal to 18 is adult.
# if age >= 18:
#     age_group = "Adult"
# else:
#     age_group = "Child"

# # applicant_type:str should be age goup with the member status like "Adult Member" or "Child Non-member"
# # write the whole if else block
# if is_member:
#     if age >= 18:
#         applicant_type = "Adult Member"
#     else:
#         applicant_type = "Child Member"
# else:
#     if age >= 18:
#         applicant_type = "Adult Non-member"
#     else:
#         applicant_type = "Child Non-member"


# # part 3 


# # based on the value of `color_code` assign the `color` value in lower case and "black" if `color_code` is none of R, B and G

# if color_code == "R":
#     color = "red"
# elif color_code == "G":
#     color = "green"
# elif color_code == "B":
#     color = "blue"
# else:
#     color = "black"

# # is_time_valid = ... # bool: True if time is valid (should be ranging from 1 - 12 both including) else False 
# if 1 <= int(time[0:2]) <= 12:
#     is_time_valid = True
# else:
#     is_time_valid = False

# time = "02 PM"
# # # time_in_hrs:int should have the time in 24 hrs format . Try to do this in a single expression
# # time convert into 24 hr format

# time_in_hrs = int(time[:2]) % 12 + (12 if "PM" in time else 0)
# + 12 

# # # time_of_day:str should have the time of the day as Morning, etc.. use "Invalid" if not withing the acceptable range

# # # write your code here


# if time_in_hrs >= 6 and time_in_hrs < 12:
#     time_of_day = "Morning"
# elif time_in_hrs >= 12 and time_in_hrs < 18:
#     time_of_day = "Afternoon"
# elif time_in_hrs >= 18 and time_in_hrs < 24:
#     time_of_day = "Evening"
# elif time_in_hrs >= 0 and time_in_hrs < 6:
#     time_of_day = "Night"
# else:
#     time_of_day = "Invalid"

main_dish = input()
time_of_day = int(input())
has_voucher = input()
is_card_payment = input()

if main_dish  == "panner tikka":
    cost = 250
elif main_dish  == "butter chikcen":
    cost = 240
elif main_dish == "masal dosa":
        cost = 200
else: # if main dish is invalid print invalid dish and exit the code.
    print("Invalid main dish")
    exit() 

if time_of_day >= 12 and time_of_day <= 15:
    total_cost = cost * 0.8

else:
    total_cost = cost

if has_voucher:
    total_cost = total_cost * 0.9 # Apply voucher discount

if is_card_payment:  # service charge for card payments
    service_charge = 0.05 * total_cost
    total_cost =+ service_charge

    print(f"{total_cost:.02f}")
