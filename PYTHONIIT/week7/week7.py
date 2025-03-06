
def most_occuring_first_letter(passage: str) -> str:
    '''
    Returns the letter which occurs most frequently 
    as the first letter of any word.(case insensitive)

    Args:
        passage (str): A multi-line string representing the passage.

    Returns:
        str: The most frequently occurring first letter in lowercase.
    '''
    l = list(passage)
     
    l1 = []
    for i in range(len(l)):
        if l[i] == '\n' and i == 0:
            continue
        if l[i] == '\n':
            l1.append(" ")
        else:
            l1.append(l[i])
    
    str1 = ""
    for i in l1:
        str1 = str1 + i
        
    l = str1.split(" ")
    
    d = {}
    print(l)
    
    for i in l:
        if i == "":
            continue
        if i[0] in d:
            d[i[0]] = d[i[0]] + 1
        else:
            d[i[0]] = 1
    
    final = ""
    count = 0
    for i in d:
        if d[i] > count:
            count = d[i]
            final = i
    return final     
        
            
    
        
        
        
        
        
        
        
        
        
        
        
        
        

