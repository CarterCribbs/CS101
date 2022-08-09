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
    lst = []
    movielist =[]
    file = os.path.join("data", "movies.txt")
    f = open(file)
    stripspaces = [space.strip() for space in f]
    dict = {}

    for item in stripspaces:
        lst.append(item.split(","))
    lstsorted = sorted(lst, key=lambda x:(x[0],x[1]))
    for item in lstsorted:
        movielist.append(item[1])
    setmovies = set(movielist)
    lst = sorted(list(setmovies))


    for item in lst:
        if item[0] not in dict:
            dict[item[0]]=[]
    lst = sorted(lst, key=lambda x:(x[1],x[0]))
    length = len(movielist)
    for item in range(length):
        for object in lst:
            if object[1]==movielist[item]:
                rate = object[2]
                dict[object[0]].append(rate)
        for (x,y) in dict.items():
            if len(y)==item:
                dict[x].append(0)
    f.close()
    return (movielist, dict)


