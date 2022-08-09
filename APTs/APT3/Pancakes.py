"""
Created on 10/3/21

@author: cartercribbs
"""

def minutesNeeded(numCakes, capacity):
    if numCakes % capacity == 0:
        return 10 * (numCakes//capacity)
    elif numCakes % capacity > capacity / 2:
        return 10 * (numCakes//capacity) + 10
    else:
        return 10 * (numCakes//capacity) + 5


'''
def minutesNeeded(numCakes, capacity)
    full = numCakes//capacity
    left = numCakes % capacity
    minutes = 10 * full
    if left > capacity/2:
        minutes += 10
    elif left > 0:
        minutes +=5
    return minutes






if __name__ == '__main__':
    numCakes = 3
    capacity = 2
    print(minutesNeeded(numCakes, capacity))
'''