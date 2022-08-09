

import random



if __name__ == '__main__':
    secretword = "houses"
    hangmanWord = []
    lengthofword = len(secretword)
    for item in range(lengthofword):
        hangmanWord.append("_")
    print(hangmanWord)
