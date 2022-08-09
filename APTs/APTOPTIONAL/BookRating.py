"""
Created on 10/9/21

@author: cartercribbs
"""

def calculate(readpages, totalpages, numdays, amazon):
    answer = ((((readpages/totalpages)*1000)/numdays)**2 +(amazon)**2)**(1/2)
    finalresult = int(answer)
    return finalresult
if __name__ == '__main__':
    readpages = 356
    totalpages = 356
    numdays = 10
    amazon = 4.12
    print(calculate(readpages, totalpages, numdays, amazon))
