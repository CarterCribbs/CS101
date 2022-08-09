"""
Created on 10/9/21

@author: cartercribbs
"""

def countwords(phrase, ending, item):
    wordslist = phrase.split()
    wordcount = 0
    for word in wordslist:
        if ending in word and item not in word:
            wordcount += 1
    return wordcount

if __name__ == '__main__':
    phrase = "swim trim shop drop swap rim"
    ending = "im"
    item = "sw"
    print(countwords(phrase, ending, item))
