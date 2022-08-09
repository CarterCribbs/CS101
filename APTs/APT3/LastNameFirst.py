"""
Created on 9/29/21

@author: cartercribbs
"""

def modify(name):
    splitname = name.split()
    if len(splitname) == 1:
        return name
    elif len(splitname) == 2:
        nomiddle = splitname[1] + ", " + splitname[0]
        return nomiddle
    else:
        middlenames = ""
        for item in splitname[1:-1]:
            if len(item) == 1:
                middlenames += item + " "
            else:
                abbreviate = item[0] + "." + " "
                middlenames += abbreviate
        resultwithextraspace = splitname[-1] + ", " + splitname[0] + " " + \
                          middlenames
        return resultwithextraspace[:-1]

'''
if __name__ == '__main__':
    name = "Liz A Bo To Joe"
    print(modify(name))
'''