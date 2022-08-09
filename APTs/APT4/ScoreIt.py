"""
Created on 10/12/21

@author: cartercribbs
"""



def maxPoints(toss):
    scorelist = []
    for number in toss:
        numberofoccurances = toss.count(number)
        score = numberofoccurances*number
        scorelist.append(score)
    return max(scorelist)


'''
if __name__ == '__main__':
    toss = [ 5, 3, 5, 3, 3 ]
    print(maxPoints(toss))
'''
