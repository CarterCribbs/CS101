"""
Created on 11/8/21

@author: cartercribbs
"""


def whosDishonest(club1, club2, club3):
    namelist = []
    for item in club1:
        if item in club2 or item in club3:
            namelist.append(item)
    for item in club2:
        if item in club3:
            namelist.append(item)
    namelistset = set(namelist)
    namelistlist = list(namelistset)
    sortednames = sorted(namelistlist)
    return sortednames


