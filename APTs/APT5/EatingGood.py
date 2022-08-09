"""
Created on 10/24/21

@author: cartercribbs
"""

def howMany(meals, restaurant):
    listofeaters = set()
    for item in meals:
        listsplit = item.split(":")
        if listsplit[1] == restaurant:
            listofeaters.add(listsplit[0])
    return len(listofeaters)

'''
if __name__ == '__main__':
    meals = ["Sue:Elmos", "Joe:Mad Hatter", "Sue:Mad Hatter", "Kristin:Sitar"]

    restaurant = "Mad Hatter"
    print(howMany(meals, restaurant))
'''