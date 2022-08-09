"""
Created on 11/8/21

@author: cartercribbs
"""


def freqs(data):
    itemcountlist = []
    itemlist = []
    sorteddata = sorted(data)
    for item in sorteddata:
        if item not in itemlist:
            itemlist.append(item)
            itemcount = data.count(item)
            itemcountlist.append(itemcount)
    return itemcountlist
