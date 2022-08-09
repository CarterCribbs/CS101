"""
Created on 10/12/21

@author: cartercribbs
"""
def toTen(lstOp, lstNum):
    lstOpcount= 0
    placecount  = 0
    totalcount = 0
    lengthlstOp = len(lstOp)
    lengthlstNum = len(lstNum)
    while totalcount!=10:
        if placecount == lengthlstOp or placecount==lengthlstNum:
            return -1
        if lstOp[placecount] == "+":
            totalcount += lstNum[placecount]
        elif lstOp[placecount] == "-":
            totalcount -= lstNum[placecount]
        elif lstOp[placecount] == "*":
            totalcount *= lstNum[placecount]
        elif lstOp[placecount] == "/":
            totalcount /= lstNum[placecount]
        placecount += 1
        lstOpcount += 1
    return lstOpcount

'''
if __name__ == '__main__':
    lstOp = ['-']
    lstNum = [-5, 5]
    print(toTen(lstOp, lstNum))
'''