"""
Created on 10/3/21

@author: cartercribbs
"""

def acronym(phrase):
    listofwords = phrase.split()
    acronym = ""
    for word in listofwords:
        firstletter = word[0]
        acronym += firstletter
    return acronym

'''
if __name__ == '__main__':
    phrase = 'Johnnys Fried Chicken on 7th Avenue is the best!'
    print(acronym(phrase))
'''