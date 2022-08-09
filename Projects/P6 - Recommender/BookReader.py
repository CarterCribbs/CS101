'''
@author: Carter Cribbs
'''

import os
def getdata():
    '''
    This function reads data from a file and returns the data in the form of a two-tuple.
    The first element of the two-tuple is a list of strings, the second element is a 
    dictionary.
    '''
    booklist = []
    dict ={}
    file = os.path.join("data", "books.txt")
    f=open(file)
    strip=[word.strip() for word in f]
    for item in strip:
        dicttwo={}
        split = item.split(",")
        book = split[0]
        if book not in dict:
            dict[book] = []
        for object in range(1, len(split)):
            if object % 2 != 0:
                dicttwo[split[object]] =int(split[object+1])
                if split[object] not in booklist:
                    booklist.append(split[object])
        for (x,y) in dicttwo.items():
            dict[book].append(y)
    f.close()
    return(booklist, dict)

