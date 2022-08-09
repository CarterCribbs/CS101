"""
Created on 11/5/21

@author: cartercribbs
"""

def winners(ballot):
        votesDict = {}
        for elem in ballot:
            lst = elem.split()
            for i in range(len(lst)):
                    if lst[i] not in votesDict:
                        votesDict[lst[i]] = 0
                    votesDict[lst[i]] += len(lst) - i
        Max = max(votesDict.values())
        ret = []
        for k, v in votesDict.items():
            if v == Max:
                ret.append(k)
        return sorted(ret)



