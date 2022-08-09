"""
Created on 10/14/21

@author: cartercribbs
"""



if __name__ == '__main__':
    lst1 = [10,11,12, ["a", "b"]]
    lst2 = lst1[:]
    lst2[0] = 100
    lst2[3].append("c")
    print(lst1)
    print(lst2)