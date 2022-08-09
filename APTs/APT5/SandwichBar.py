"""
Created on 10/26/21

@author: cartercribbs
"""


def whichOrder(available, orders):
    checkifmatch = 0
    for item in orders:
        ingridient = item.split()
        for element in ingridient:
            if element in available:
                checkifmatch +=1
        if checkifmatch == len(ingridient):
            index = orders.index(item)
            return index
        else:
            checkifmatch = 0
    return -1


'''
if __name__ == '__main__':

    available = ["cheese", "mustard", "lettuce"]

    orders = ["cheese ham", "cheese mustard lettuce", "ketchup", "beer"]
    print(whichOrder(available, orders))
'''
