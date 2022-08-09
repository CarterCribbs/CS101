"""
Created on 11/22/21

@author: cartercribbs
"""



def bestInvitation(first,second):
    totallist = []

    for item in first:
        countfirst = first.count(item)
        countsecond = second.count(item)
        totalcount = countfirst + countsecond
        totallist.append(totalcount)
    for item in second:
        secondcount = second.count(item)
        totallist.append(secondcount)
    maxcount = max(totallist)
    return maxcount

