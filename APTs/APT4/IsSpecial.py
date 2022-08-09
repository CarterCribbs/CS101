"""
Created on 10/12/21

@author: cartercribbs
"""

def lovely(ingredients, inedible):
    lstofinedible = inedible.split()
    lstofingredients = ingredients.split()
    inediblenumber = 0
    totalingredients = len(lstofingredients)
    for item in lstofinedible:
        if item in ingredients:
            inediblenumber+=1
    return totalingredients - inediblenumber

'''
if __name__ == '__main__':
    ingredients = "milk sugar chocolate"
    inedible = "milkchocolate"
    print(lovely(ingredients, inedible))
'''