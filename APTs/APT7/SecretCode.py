"""
Created on 11/19/21

@author: cartercribbs
"""



def decrypt(message, numbers):
    index = 0
    string = ""
    messagesplit = message.split()
    for item in messagesplit:
        if numbers[index] < 0:
            if numbers[index] >= (len(item)*-1):
                string += item[numbers[index]]
        elif numbers[index] < len(item):
            string += item[numbers[index]]
        index +=1
    return string