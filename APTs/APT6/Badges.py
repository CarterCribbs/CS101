"""
Created on 11/5/21

@author: cartercribbs
"""

def findLabel(labels,deeds,needs):

    indexvalue = 0
    for item in needs:
        needlist = item.split()
        checkcount = 0
        for item in needlist:
                if item in deeds:
                    checkcount +=1
        if checkcount == len(needlist):
            return labels[indexvalue]
        else:
            checkcount = 0
            indexvalue += 1
    return "nobadge"




if __name__ == '__main__':
    labels = ['first', 'second', 'third', 'fourth']
    deeds = ['code', 'talk', 'plan', 'run']
    needs = ['code talk plan think', 'talk plan run ', 'plan run code think', 'run code talk think']
    print(findLabel(labels, deeds, needs))

