"""
Created on 10/9/21

@author: cartercribbs
"""

def computeSubjects(phrase):
    wordlist = phrase.split()
    newlist = []
    for item in wordlist:
        if ":" not in item and "-" not in item and "1234567890" not in item:
            newlist += item
    result = ''.join(newlist)
    return result
if __name__ == '__main__':
    phrase = "CompSci 101 TuTh1:25pm Econ 101 MW10:05am"
    print(computeSubjects(phrase))
