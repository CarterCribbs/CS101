"""
Created on 10/24/21

@author: cartercribbs
"""


def bags(food, strength):
    d = {}
    for type in food:
        if type in d:
            d[type] +=1
        else:
            d[type] =1
    listofnumbers = list(d.values())
    index = 0
    totalcount = 0
    print(listofnumbers)
    for item in listofnumbers:
        if item % strength ==0:
            totalcount += item/strength
        else:
            totalcount += item // strength +1
    return int(totalcount)




if __name__ == '__main__':
    strength = 2

    food = ["CANNED", "CANNED", "PRODUCE", "DAIRY", "MEAT", "BREAD", "HOUSEHOLD", "PRODUCE", "FROZEN", "PRODUCE", "DAIRY"]

    print(bags(food, strength))


