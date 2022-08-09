"""
Created on 9/29/21

@author: cartercribbs
"""

def repeat(word, number):
    print("carter" *3)
    vowels = "AEIOUaeiou"
    if len(word) >= 3:
        if word[0] in vowels:
            return word
        elif word[0] not in vowels and word[1] not in vowels and word[
            2] not in vowels:
            return word
        elif word[2] in vowels:
            thirdlettervowel = word[0:3] + word[0:3].lower() * (number-1) + \
                           word[3:]
            return thirdlettervowel
        elif word[2] not in vowels and word[1] in vowels:
            thirdletternotvowelsecondlettervowel = word[0:2] + word[0:2].lower() * \
                                               (number-1) + word[2:]
            return thirdletternotvowelsecondlettervowel
        else:
            return word
    elif len(word) == 2:
        if word[1] in vowels:
            secondlettervowel = word[0:2] + word[0:2].lower() * \
                                (number - 1) + word[2:]
            return secondlettervowel
        else:
            return word
    else:
        return word


'''

if __name__ == '__main__':

    word = "Ba"
    number = 5
    print(repeat(word, number))
'''