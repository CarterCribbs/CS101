"""
Created on 10/18/21

@author: cartercribbs
"""


import os.path

shift = 5
lower_alph = "abcdefghijklmnopqrstuvwxyz"
upper_alph = lower_alph.upper()
shifted_lower = lower_alph[5:] + lower_alph[:5]
shifted_upper = upper_alph[5:] + upper_alph[:5]


def encrypt(w):
    '''
    This function takes words as an input and
    shifts all the characters by a certain
    number to encrypt them.
    '''
    newstring= ""
    for char in w:
        if char in lower_alph:
            charindex = lower_alph.index(char)
            char = (shifted_lower[charindex])
            newstring+= char
        elif char in upper_alph:
            charindex = upper_alph.index(char)
            char = (shifted_upper[charindex])
            newstring += char
        else:
            newstring += char
    return newstring

def setShift(shiftednumber):
    '''
    This function sets the global variables used in
    encrypt.
    '''
    global shift
    global shifted_lower
    global shifted_upper
    shift = shiftednumber
    shifted_lower = lower_alph[shiftednumber:] + lower_alph[:shiftednumber]
    shifted_upper = upper_alph[shiftednumber:] + upper_alph[:shiftednumber]

def findShift(input):
    '''
    This function takes an input of words encrypted by
    a shift and returns the value the characters
    were shifted by.
    '''
    file = os.path.join("data", "lowerwords.txt")
    f = open(file)
    wordsClean = [w.strip() for w in f.read().split()]
    overlaplist = []
    for i in range(26):
        setShift(i)
        encryption = [encrypt(w) for w in input.split()]
        overlap = set(wordsClean) & set(encryption)
        overlaplist.append(len(overlap))
    maximumindex = max(overlaplist)
    shiftvalue = overlaplist.index(maximumindex)
    f.close()
    return 26 - shiftvalue


if __name__ == '__main__':
    setShift(15)
    w = "bar stool happy cat"
    print(encrypt(w))
    print(findShift("qpg hidda wpeen rpi"))
    setShift(3)
    w = "my name is Carter"
    print(encrypt(w))
    print(findShift("pb qdph lv Fduwhu"))
    setShift(23)
    print(encrypt("pb qdph lv Fduwhu"))

