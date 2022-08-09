"""
Created on 9/26/21

@author: cartercribbs
"""

def combine(first, flen, second, slen):
    result = first[0:flen] + second[-slen:]
    return result
'''
if __name__ == '__main__':
    first = "stay"
    flen = 4
    second = "vacation"
    slen = 6
    print(combine(first, flen, second, slen))
'''