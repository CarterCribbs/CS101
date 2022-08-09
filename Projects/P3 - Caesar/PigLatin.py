"""
Created on 10/10/21

@author: cartercribbs
"""

def encrypt(word):
    '''
    This function takes a word and turns it into
    pig latin using pig latin language rules.
    '''
    vowels = "AEIOUaeiou"
    vowelsaddy = "AEIOUYaeiouy"
    if word[0] in vowels:
        return word + "-way"
    elif word[0] in "yY":
        lettercount = 0
        for char in word:
            if char in vowels:
                break
            lettercount+=1
        newword = word[lettercount:] + "-" + word[:lettercount] + "ay"
        return newword
    elif word[0] in "qQ" and word[1] in "uU":
        quword = word[2:]
        lettercount = 0
        for char in quword:
            if char in vowelsaddy:
                break
            lettercount += 1
        newword = quword[lettercount:] + "-qu" + quword [:lettercount] + "ay"
        return newword
    elif word[0] not in vowels:
        numberofvowels = 0
        for char in word:
            if char in vowelsaddy:
                numberofvowels += 1
        if numberofvowels == 0:
            newword = word + "-way"
            return newword
        lettercount = 0
        for char in word:
            if char in vowelsaddy:
                break
            lettercount+=1
        newword = word[lettercount:] +"-" + word[:lettercount]+"ay"
        return newword



def decrypt(word):
    '''
    decrypts a word given in piglatin to
    regular english
    '''
    if word[-4:] == "-way":
        return word[:-4]
    else:
        dashindex = word.find("-")
        afterdashword = word[dashindex+1:-2]
        return afterdashword + word[0:dashindex]


if __name__ == '__main__':
    print(encrypt("happy"))
    print(decrypt("appy-hay"))
    print(encrypt("yummy"))
    print(decrypt("ummy-yay"))



