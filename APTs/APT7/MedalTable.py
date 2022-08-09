"""
Created on 11/19/21

@author: cartercribbs
"""

def generate(results):
    """
    return list of strings
    based on data in results, a list of strings
    """
    Final = []
    listfinal = []
    listcountry = []
    final = []


    for i in results:
        x = i.split()
        listfinal.append(x)

    for i in listfinal:
        for x in i:
            if x not in listcountry:
                listcountry.append(x)

    for i in listcountry:
        final.append([i, 0, 0, 0])

    for x in final:
        for i in listfinal:
            if x[0] == i[0]:
                x[1] += 1
            if x[0] == i[1]:
                x[2] += 1
            if x[0] == i[2]:
                x[3] += 1

    x = sorted(final, key=lambda final: final[0])
    y = sorted(x, key=lambda x: x[3], reverse=True)
    z = sorted(y, key=lambda y: y[2], reverse=True)
    tut = sorted(z, key=lambda z: z[1], reverse=True)

    for item in tut:
        newlist = ""
        for x in item:
            newlist += str(x) + " "
        Final.append(newlist[0:-1])
    return Final




