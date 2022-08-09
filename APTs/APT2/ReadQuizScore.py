"""
Created on 9/26/21

@author: cartercribbs
"""

def grade(total, availablepoints, cutOff):
    if (total/availablepoints)*100>= cutOff:
        return 100.0
    else:
        result = ((total/(availablepoints*(cutOff*0.01)))*100)
        return result

'''
if __name__ == '__main__':
    total= 6
    availablepoints= 16
    cutOff = 75
    print(grade(total, availablepoints, cutOff))
'''