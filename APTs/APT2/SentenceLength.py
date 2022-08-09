"""
Created on 9/26/21

@author: cartercribbs
"""
'''
def average(sentencelist):
    wordsinsentence = 0
    for item in sentencelist:
        wordsinitem = item.split()
        wordsinindividualsentence = wordsinitem.count(" ") + 1
        wordsinsentence = wordsinsentence + wordsinindividualsentence
    numberofsentences = len(sentencelist)
    test = sentencelist.count("t")
    print(test)
    result = wordsinsentence/numberofsentences
    return result

if __name__ == '__main__':
    
    sentencelist = ["the", "only way", "we can get", "all green is to", "fail"]
    print(average(sentencelist))


'''
'''
def average(sentencelist):
    numberofwords = 0
    for item in sentencelist:
        wordsinitem = (len(item.split()))
        numberofwords = numberofwords + wordsinitem
    numberofsentences = len(sentencelist)
    result = numberofwords/numberofsentences
    return result


if __name__ == '__main__':
    sentencelist = ["the", "only way", "we can get", "all green is to", "fail"]
    print(average(sentencelist))
'''

def counting(sentencelist):
    test = sentencelist.count("t")
    return test

if __name__ == '__main__':
    sentencelist = ["the", "only way", "we can get", "all green is to", "fail"]
    print(counting(sentencelist))



