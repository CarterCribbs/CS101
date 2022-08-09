'''
@author: Carter Cribbs
'''

def averages(items, ratings):
    '''
    This function calculates the average ratings for items. 
    A two-tuple is returned, where the first element is a string and the second element is a float.
    '''
    total = 0
    denominator = 0
    tuplelist = []
    valueslist = []
    itemlength = len(items)
    for object in ratings.values():
        valueslist.append(object)
    for item in range(itemlength):
        valuelistlength = len(valueslist)
        for thing in range(valuelistlength):
            total += valueslist[thing][item]
            if valueslist[thing][item] != 0:
                denominator +=1
        if denominator ==0:
            denominator =1
        tuplelist.append((items[item], float(total/denominator)))
        total = 0
        denominator = 0
    sortedlist = sorted(tuplelist, key=lambda x:x[0])
    return sorted(sortedlist, key=lambda x:x[1], reverse=True)



def similarities(name, ratings):
    '''
    This function calculates how similar the rater called name is to all other raters.
    A two-tuple is returned, where the first element is a string and the second element is an integer.
    '''
    dotproduct = 0
    userlist = []
    totallist = []
    for object in ratings[name]:
        userlist.append(object)

    for object in ratings.items():
        if object[0] != name:
            ratinglength = len(object[1])
            for counter in range(ratinglength):
                dotproduct += int(userlist[counter])*int(object[1][counter])
            totallist.append((object[0], dotproduct))
            dotproduct = 0
    sortedlist = sorted(totallist, key=lambda x:x[0])
    sortedagain = sorted(sortedlist, key=lambda x:x[1], reverse=True)
    return sortedagain



def recommendations(name, items, ratings, numUsers):
    '''
    This function calculates the weighted average ratings and makes recommendations 
    based on the parameters and weighted average. A two-tuple is returned, where 
    the first element is a string and the second element is a float.
    '''

    newratings = {}
    similarityoutput = similarities(name, ratings)
    for item in range(numUsers):
        list =[]
        for x in ratings[similarityoutput[item][0]]:
            list.append(similarityoutput[item][1]*x)
        newratings[similarityoutput[item][0]] = list
    return averages(items, newratings)


