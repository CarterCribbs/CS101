"""
Created on 11/19/21

@author: cartercribbs
"""

def nameDonor(contributions):
    namedict = {}
    for i in contributions:
        contributionsplit = i.split(":")
        if contributionsplit[0] not in namedict:
            namedict[contributionsplit[0]] = 0
        namedict[contributionsplit[0]] += float(contributionsplit[1])

    peoplesorted = sorted(namedict.items())
    donationssorted = sorted(peoplesorted, key=lambda x: x[1], reverse = True)

    return donationssorted[0][0]