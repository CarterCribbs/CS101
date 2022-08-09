"""
Created on 9/26/21

@author: cartercribbs
"""




def shorten(name):
    namelist = name.split()
    if len(namelist) == 1:
        return name

    else:
        result = str(namelist[0]) + str(' ') + str(namelist[-1])
        return result

'''

if __name__ == '__main__':
    name = "Michelle abf add Obama"
    print(shorten(name))
'''