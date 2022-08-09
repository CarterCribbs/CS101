"""
Created on 10/3/21

@author: cartercribbs
"""

def bagelCount(orders):
    totalbagels = 0
    for item in orders:
        if item < 12:
            totalbagels += item
        else:
            totalbagels += item + item//12
    return totalbagels


'''
if __name__ == '__main__':
    orders = [11,22,33,44,55]
    print(bagelCount(orders))
'''