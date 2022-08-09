"""
Created on 9/5/21

@author: cartercribbs
"""

def score(word):
    stringlengthsquared = (len(word))**2
    return stringlengthsquared

if __name__ == '__main__':
    word = "catata"
    print(score(word))
