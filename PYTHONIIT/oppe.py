def get_roll_nos(data,criteria=None):
    avg = 0
    sum1 = 0
    for i in data:
        sum1 += i[1]
    avg = sum1/len(data)

    if criteria == "above_average":
        new_list =[]
        for i in data:
            if i[1] > avg:
                new_list.append(i[0])
        return new_list        
    if criteria == "below_average":
        new_list =[]
        for i in data:
            if i[1] < avg:
                new_list.append(i[0])
        return new_list
    else:
        new_list = []
        for i in data:
            if i[1] == avg:
                new_list.append(i[0])
        return new_list
    
data = [('101', 85), ('102', 75), ('103', 45), ('104', 95), ('105', 35)]

# print(get_roll_nos(data,"above_average"))


#p2

def is_positive_odd_or_negative_even(n: int) -> bool:
    '''Check if the number is a positive odd or a negative even.

    Args:
        n : int - input integer

    Returns:
        bool - True if positive odd or negative even, else False
    '''
    if (n> 0 and n%2  != 0) or (n< 0 and n%2 == 0):
        return True
    else:
        return False
    


# print(is_positive_odd_or_negative_even(5))

def within_and_has_double_quotes(s: str) -> bool:
    '''Check if the string is enclosed with double quotes and has double quotes inside.

    Args:
        s : str - input string

    Returns:
        bool - True if the string starts and ends with double quotes and has double quotes inside
    '''
    l = list(s)
  
    c= 0
    for i in l:
        if i == '"':
            c += 1
    if c >=3:
        return True
    else:
        return False

# print(within_and_has_double_quotes('abcd"efgh'))

def replace_middle_with_n_times_middle(t: tuple, n: int) -> tuple:
    '''
    Replace the middle element of a tuple with `n` copies of the middle element.

    Args:
        t (tuple): A tuple with an odd number of elements.
        n (int): The number of times the middle element should be repeated.

    Returns:
        tuple: A new tuple with the middle element replaced by `n` copies.
    '''
    l = list(t)
    mid = len(t)//2
    element = l[mid]
    for i in range(n):
        l.insert(mid,element)
        mid += 1

    t = tuple(l)
    return t    

# print(replace_middle_with_n_times_middle((1, 2, 3, 4, 5),5))

def count_positive_ignore_none(nums: list):
    '''
    Count the number of positive integers in the list, ignoring `None` values and zeros.

    Args:
        nums (list): A list of numbers, possibly containing `None` values.

    Returns:
        int: The count of positive integers in the list.
    '''
    count =  0
    for i in nums:
        if i != None and i != 0 :
            if i > 0:
                count += 1
    return count
    
# count_positive_ignore_none()

def div_by_exactly_one(num: int, a: int, b: int) -> bool:
    '''Check if num is divisible by exactly one of a or b.

    Args:
        num, a, b : int - input numbers

    Returns:
        bool - True if num is divisible by exactly one of a or b, otherwise False.
    '''
    if num % a == 0 or num % b == 0:
        return True
    else:
        return False
    
