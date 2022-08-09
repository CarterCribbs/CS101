"""
Created on 11/22/21

@author: cartercribbs
"""


def difference(strengths):
    teamone = []
    teamtwo = []
    sortedstrengths = sorted(strengths, reverse=True)
    indexcount = 0
    for item in sortedstrengths:
        if indexcount % 2 == 0:
            teamone.append(item)
        else:
            teamtwo.append(item)
        indexcount +=1
    sumteamone = sum(teamone)
    sumteamtwo = sum(teamtwo)
    return (sumteamone - sumteamtwo)