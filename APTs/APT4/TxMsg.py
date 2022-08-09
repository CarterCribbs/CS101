"""
Created on 10/12/21

@author: cartercribbs
"""

def transform(word):
    indexcount = 1
    consonantcount = 0
    consonants = "bcdfghjklmnpqrstvwxyz"
    newstring =""
    for item in word:
        if item in consonants:
            consonantcount +=1
    if consonantcount == 0:
        return word
    for item in word[1:]:
        if word[indexcount] in consonants and word[indexcount-1] not in consonants:
            newstring += item
        indexcount +=1
    if word[0] in consonants:
        firstconsonant = word[0]
        finalresult = firstconsonant + newstring
        return finalresult
    else:
        finalresult = newstring
        return finalresult

def getMessage(original):
    ret = []
    wordlist = original.split()
    for word in original.split():
        ret.append(transform(word))
    return " ".join(ret)


if __name__ == '__main__':
    original = "us"
    print(getMessage(original))
