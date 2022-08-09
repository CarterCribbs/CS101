"""
Created on 11/8/21

@author: cartercribbs
"""

def score(listA,listB,listC):
    scoreA = 0
    scoreB = 0
    scoreC = 0
    for item in listA:
        if item not in listB and item not in listC:
            scoreA += 3
        elif item in listB and item not in listC:
            scoreA +=2
        elif item in listC and item not in listB:
            scoreA += 2
        elif item in listC and item in listB:
            scoreA +=1
    for item in listB:
        if item not in listA and item not in listC:
            scoreB += 3
        elif item in listA and item not in listC:
            scoreB +=2
        elif item in listC and item not in listA:
            scoreB += 2
        elif item in listC and item in listA:
            scoreB +=1
    for item in listC:
        if item not in listA and item not in listB:
            scoreC += 3
        elif item in listA and item not in listB:
            scoreC +=2
        elif item in listB and item not in listA:
            scoreC += 2
        elif item in listB and item in listA:
            scoreC +=1
    return str(scoreA)+"/"+str(scoreB)+"/"+str(scoreC)


