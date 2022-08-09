'''
@author: Carter Cribbs
'''

import RecommenderEngine

def makerecs(name, items, ratings, numUsers, top):

    '''
    This function calculates the top recommendations and returns a two-tuple consisting of two lists. 
    The first list is the top items rated by the rater called name (string).
    The second list is the top items not seen/rated by name (string)
    '''
    lst = []
    lsttwo = []
    recs = RecommenderEngine.recommendations(name, items, ratings, numUsers)
    x = 0
    while x < len(recs) and (len(lst) < top or len(lsttwo) < top):
        object = recs[x][0]
        idx = items.index(object)
        if ratings[name][idx] != 0 and len(lst) < top:
            lst.append(recs[x])
        if ratings[name][idx] == 0 and len(lsttwo) < top:
            lsttwo.append(recs[x])
        x += 1
    return lst, lsttwo
