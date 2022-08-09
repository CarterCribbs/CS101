"""
Created on 12/3/21

@author: cartercribbs
"""


def maximumFacts(suspects):
    list = []
    for i in suspects:
        list.append(i.split(','))
    if len(list) == 1:
        return 0
    final = 0
    length = len(list)
    for i in range(length):
        new = set(list[i])
        for item in list[:i]:
            if len (new & set(item)) > final:
                final = len(new & set(item))
        for item in list[i+1:]:
            if len(new & set(item)) > final:
                final = len(new & set(item))
    return final

