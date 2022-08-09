"""
Created on 9/29/21

@author: cartercribbs
"""

def ratio(dna):
    numberofc = dna.count("c")
    numberofg = dna.count("g")
    totalnucleotide = len(dna)
    result = (numberofc + numberofg) / totalnucleotide
    return result

'''
if __name__ == '__main__':
    dna = "cgggggcccgggcgcgcccgggggg"
    print(ratio(dna))
'''