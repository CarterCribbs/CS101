"""
Created on 11/22/21

@author: cartercribbs
"""



def getStats(sentence):
    listcount = []
    finallist = []
    numberlist = []
    lowercase = sentence.lower()
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for item in alphabet:
        count = lowercase.count(item)
        listcount.append(count)
    sortedlist = sorted(listcount)
    if 0 not in listcount:
        numberlist.append(0)
    for item in sortedlist:
        if item not in finallist:
            numbercount = sortedlist.count(item)
            finallist.append(item)
            numberlist.append(numbercount)
    return numberlist