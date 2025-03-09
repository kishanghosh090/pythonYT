# # f = open('text.txt', 'w')

# # f = open('text.txt', 'a')

# # f.write("\nkishan\n")
# # f.write("Rana\n")
# # f.write("Ghosh\n")


# f = open('text.txt', 'r')

# # print(f.read(10))

# # print(f.readline())

# print(f.seek(1))
# print(f.read())


def getNumToWord(mat):
    d = {
        0: "one",
        1:"one",
        2:"two",
        3:"three",
        4:"four",
        5:"five",
        6:"six",
        7:"seven",
        8:"eight",
        9:"nine"
    }
    ol = []
    il = []
    
    for i in mat:
        for el in i:
            il.append(d[el])
        
        ol.append(il)
        il = []
    
    return ol

def printIntoFile(l):
    f = open("words.csv","w")
    
    for i in l:
        print(i,len(i))
        for index in range(len(i)):
            
            if index != len(i) - 1:
                
                f.write(f'{i[index]},')
                
            else:
                f.write(f'{i[index]}\n')
            
    
    

def num_to_words(mat):
    """
    Convert matrix to file

    Argument: 
        mat: list of lists
    Return:
        None
    """
    

    
    l = getNumToWord(mat)
    printIntoFile(l)
    
    
num_to_words([[1,2,3],[4,5,6]])    
    