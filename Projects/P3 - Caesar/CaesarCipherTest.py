"""
Created on 10/12/21

@author: cartercribbs
"""

import os.path

shift = 5
lower_alph = "abcdefghijklmnopqrstuvwxyz"
upper_alph = lower_alph.upper()
shifted_lower = lower_alph[5:] + lower_alph[:5]
shifted_upper = upper_alph[5:] + upper_alph[:5]


def encrypt(w):
    newstring= ""
    for char in w:
        if char in lower_alph:
            charindex = lower_alph.index(char)
            char = (shifted_lower[charindex])
            newstring+= char
        elif char in upper_alph:
            print("hi")
            charindex = upper_alph.index(char)
            char = (shifted_upper[charindex])
            newstring += char
        else:
            newstring += char
    return newstring

def setShift(shiftednumber):
    global shift
    global shifted_lower
    global shifted_upper
    shift = shiftednumber
    shifted_lower = lower_alph[shiftednumber:] + lower_alph[:shiftednumber]
    shifted_upper = upper_alph[shiftednumber:] + upper_alph[:shiftednumber]

def findShift(input):
    file = os.path.join("data", "data/lowerwords.txt")
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
    # setShift(11)
    # w = "hat crazy house"
    # print(encrypt(w))
    print(findShift("Af ugehdasfuw oalz lzw jwimwkl gx s xjawfv gx eafw, ozg ojglw ew"))


