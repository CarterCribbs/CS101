"""
Created on 10/24/21

@author: cartercribbs
"""

def theIndex(carrots, amount):
    while amount != 0:
        largestbox = max(carrots)
        carrotindex = carrots.index(largestbox)
        carrots[carrotindex] = carrots[carrotindex] - 1
        amount += -1
    return carrotindex

'''
if __name__ == '__main__':
    carrots = [5, 8]
    amount = 8
    print(theIndex(carrots, amount))
'''