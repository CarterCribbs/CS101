"""
Created on 10/24/21

@author: cartercribbs
"""


def networth(transactions):
    namelist = []
    moneylist = []
    index = 0
    for item in transactions:
        singletransaction = transactions[index].split(":")
        if singletransaction[0] not in namelist:
            namelist.append(singletransaction[0])
            moneyvalue = -1 * (int(float(singletransaction[2])*100))/100
            moneylist.append(moneyvalue)
        else:
            indexingname = namelist.index(singletransaction[0])
            moneyvalue = int(float(singletransaction[2]) * 100) /100
            moneylist[indexingname] -= moneyvalue
        if singletransaction[1] not in namelist:
            namelist.append(singletransaction[1])
            moneyvalue = int(((float(singletransaction[2])*100))) / 100
            moneylist.append(moneyvalue)
        else:
            indexingname = namelist.index(singletransaction[1])
            moneyvalue = int(float(singletransaction[2]) *100)/100
            moneylist[indexingname] += moneyvalue
        index +=1
    itemrange = 0
    for item in moneylist:
        moneylist[itemrange] = round(moneylist[itemrange], 2)
        itemrange += 1

    finallist = []
    indexfinallist = 0
    for item in namelist:
        finalitem = str(namelist[indexfinallist]) + ":" + str(moneylist[indexfinallist])
        finallist.append(finalitem)
        indexfinallist += 1
    return sorted(finallist)

'''
if __name__ == '__main__':
    transactions = ['ola:foo:13.66', 'ola:bar:0.99', 'rcd:ola:39.39', 'rcd:foo:99.99', 'rcd:foo:57.86']
    print(networth(transactions))
'''
