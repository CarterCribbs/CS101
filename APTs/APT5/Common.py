"""
Created on 10/26/21

@author: cartercribbs
"""

'''
def count(a,b):
    lista = [w for w in a]
    listb = [w for w in b]
    counting = 0
    for item in lista:
        if item in listb:
            countofletterina = lista.count(item)
            countofletterinb = listb.count(item)
            if countofletterina == countofletterinb:
                counting += countofletterina
            else:
                listofaandb = [countofletterina, countofletterinb]
                minlettercount = min(listofaandb)
                counting += minlettercount
'''



def count(a,b):
    lista = [w for w in a]
    listb = [w for w in b]
    counting = 0
    for item in lista:
        if item in listb:
            listb.remove(item)
            counting +=1
    return counting

'''
if __name__ == '__main__':
    a="horse"

    b="moose"
    print(count(a,b))
'''
