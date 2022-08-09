"""
Created on 9/26/21

@author: cartercribbs
"""

def weight3(ab, ac, bc):
    a = ((ab+ac)-(bc))/2
    b = ab - a
    c = ac - a
    result = a + b + c
    return result

'''
if __name__ == '__main__':
    ab = 200
    ac = 300
    bc = 200
    print(weight3(ab, ac, bc))
'''