"""
Created on 10/12/21

@author: cartercribbs
"""

def check(word):
    picount = word.count("pi")
    chucount = word.count("chu")
    kacount = word.count("ka")
    totalpikachuletters = 2*picount + 3*chucount + 2*kacount
    totalletterinword = len(word)
    if totalletterinword == totalpikachuletters:
        return "YES"
    else:
        return "NO"

'''
if __name__ == '__main__':
    word = "duke"
    print(check(word))
'''