"""
Created on 11/19/21

@author: cartercribbs
"""


def countVisible(trophies):
    compareforward = 0
    forwardcount =0
    comparebackward = 0
    backwardcount = 0
    for item in trophies:
        if item > compareforward:
            compareforward = item
            forwardcount += 1
    trophies.reverse()
    for item in trophies:
        if item > comparebackward:
            comparebackward = item
            backwardcount += 1
    return [forwardcount, backwardcount]

