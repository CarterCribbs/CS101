"""
Created on 11/22/21

@author: cartercribbs
"""
def winners(data):
    dict ={}
    items = []
    split =[]
    for item in data:
        items.append(item.split())
    for item in items:
        split.append([item[0], item[1].split(":")])
    for item in split:
        if item[0] not in dict:
            dict[item[0]] = [0,0,0]
        dict[item[0]][0] = dict[item[0]][0] +1
        dict[item[0]][1] = dict[item[0]][1] + int(item[1][0])
        dict[item[0]][2] = dict[item[0]][2] + int(item[1][1])
    final = sorted(dict.items(), key=lambda x:x[1][2])
    final = sorted(final, key=lambda x:x[1][1])
    final = sorted(final, key=lambda x:x[1][0], reverse=True)
    list = []
    for item in final:
        list.append(item[0])
    return list

'''

def winners(data):
    namelist = []
    namelistparallel= []
    numbercount = []
    secondslist = []
    secondnameparallel = []
    for item in data:
        datasplit = item.split()
        namelist.append(datasplit[0])

    for item in namelist:
        if item not in namelistparallel:
            count = namelist.count(item)
            namelistparallel.append(item)
            numbercount.append(int(count)*10000)

    for item in data:
        datasplit = item.split()
        secondcount = datasplit[1].split(":")
        if datasplit[0] not in secondnameparallel:
            secondslist.append(int(secondcount[0])*60 + int(secondcount[1]))
            secondnameparallel.append(datasplit[0])
        else:
            index = secondnameparallel.index(datasplit[0])
            secondslist[index] += (int(secondcount[0])*60 + int(secondcount[1]))

    index = 0
    for item in secondslist:
        numbercount[index] += item
        index +=1

    dict = {}
    for item in namelistparallel:
        index = namelistparallel.index(item)
        dict[item] = numbercount[index]

    sortedd = sorted(dict.values())
    sorteddict = {}
    for i in sortedd:
        for z in dict.keys():
            if dict[z] == i:
                sorteddict[z] = dict[z]
                break
    namelistfinal = list(sorteddict.keys())
    namelistfinal.reverse()
    return namelistfinal





    largest = 0
    largestindex = -1
    compareindex = -1
    finallist = []
    for item in numbercount:
        if item > largest:
            largest = item
            largestindex +=1
            compareindex +=1
        elif item == largest:
            compareindex +=1
                        
'''


