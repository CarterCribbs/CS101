'''
Description:
        You must create a Hangman game that allows the user to play and guess a secret word.
        See the assignment description for details.

@author: YourName Carter Cribbs    YourNetID cdc86
'''

import random


def handleUserInputDifficulty():
    '''
    This function asks the user if they would like to play the game in (h)ard or (e)asy mode, then returns the
    corresponding number of misses allowed for the game.
    '''
    print("How many misses do you want? Hard has 8 and Easy has 12.")
    choice = input("(h)ard or (e)asy> ")
    if choice == "h":
        return 8
    else:
        return 12

def handleUserInputDebugMode():
    '''
    This function asks the user if they would like to play the game in (d)ebug or (p)lay mode, then returns
    True or False depending on the users choice.
    '''
    choice = input("Which mode do you want: (d)ebug or (p)lay: ")
    if choice == "d":
        return True
    if choice == "p":
        return False

def handleUserInputWordLength():
    '''
    This function asks the user how many letter they would like to be in the secret word then returns
    the number choosen by the user.
    '''
    choice = input("How many letters in the word you'll guess: ")
    return int(choice)


def createTemplate(currTemplate, letterGuess, word):
    '''
    This function creates a new template for the secret word.
    '''
    letterindex = 0
    newtemplate = ""
    for item in word:
        if currTemplate[letterindex] != "_":
            newtemplate += item
        elif item == letterGuess:
            newtemplate += letterGuess
        else:
            newtemplate += "_"
        letterindex +=1
    return newtemplate




def getNewWordList(currTemplate, letterGuess, wordlist, debug):
    '''
    This function constructs a dictionary of string as the keys to lists as the values.
    It returns the longest value list.
    '''
    worddict = {}
    for item in wordlist:
        wordtemplate = createTemplate(currTemplate, letterGuess, item)
        if wordtemplate in worddict:
            worddict[wordtemplate].append(item)
        elif wordtemplate not in worddict:
            worddict[wordtemplate] = [item]
    dictionarylist = list(worddict.items())
    sorteddictionary = sorted(dictionarylist, key = lambda y: y[0])
    longestvaluesort = sorted(dictionarylist, key = lambda y: (len(y[1]), y[0].count("_")))


    if debug:
        for item in sorteddictionary:
            print(item[0]+" : "+str(len(item[1])))
        print("# keys = " + str(len(sorteddictionary)))
    return longestvaluesort[-1]



def processUserGuessClever(guessedLetter, hangmanWord, missesLeft):
    '''
    This function updates the number of misses left and indicates
    whether the user missed.
    '''
    if guessedLetter in hangmanWord:
        return [missesLeft, True]
    elif guessedLetter not in hangmanWord:
        return [missesLeft-1, False]


def createDisplayString(lettersGuessed, missesLeft, hangmanWord):
    '''
    Creates the string that will be displayed to the user, using the information in the parameters.
    '''
    lettersnotguessedlist = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    hangmanwordstring = ""

    for item in lettersGuessed:
        if item in lettersnotguessedlist:
            itemindex = lettersnotguessedlist.index(item)
            lettersnotguessedlist[itemindex] = " "
    lettersnotguessedstring = "".join(lettersnotguessedlist)
    for item in hangmanWord:
        hangmanwordstring += item + " "

    return "letters not yet guessed: " + str(lettersnotguessedstring) + "\nmisses remaining = " + str(
        missesLeft) + "\n" + str(hangmanwordstring) + "\n"


def handleUserInputLetterGuess(lettersGuessed, displayString):
    '''
    Prints displayString, then asks the user to input a letter to guess.
    This function handles the user input of the new letter guessed and checks if it is a repeated letter.
    '''
    while True:
        print(displayString)
        letterchoice = input("letter> ")
        if letterchoice in lettersGuessed:
            print("you already guessed that.")
        else:
            return letterchoice




def runGame(filename):
    '''
    This function sets up the game, runs each round, and prints a final message on whether or not the user won.
    True is returned if the user won the game. If the user lost the game, False is returned.
    '''
    debug = handleUserInputDebugMode()
    lettersinword = handleUserInputWordLength()
    file = open(filename, "r")
    wordList= []
    [wordList.append(wor.strip()) for wor in file if len(wor) ==(int(lettersinword) +1)]
    file.close()





    missesLeft = handleUserInputDifficulty()


    hangmanWord = ""
    for item in range(int(lettersinword)):
        hangmanWord += "_"

    missedletters = 0
    currTemplate = "_" * int(lettersinword)
    lettersGuessed = []
    while "_" in hangmanWord and missesLeft != 0:
        displayString = createDisplayString(lettersGuessed, missesLeft, hangmanWord)
        guessedLetter = handleUserInputLetterGuess(lettersGuessed, displayString)
        lettersGuessed.append(guessedLetter)
        if debug:
            wordchoice = random.choice(wordList)
            print("(word is "+wordchoice+")")
            print("# possible words: " + str(len(wordList)))
        freshlist = getNewWordList(currTemplate, guessedLetter, wordList, debug)
        processuserguess = processUserGuessClever(guessedLetter, hangmanWord, missesLeft)
        hangmanWord = freshlist[0]
        currTemplate = freshlist[0]
        wordList = freshlist[1]
        missesLeft = processuserguess[0]
        if processuserguess[1] == False:
            print("you missed: " +str(guessedLetter)+ " not in word")


        if guessedLetter not in hangmanWord:
            missedletters += 1


    if missesLeft == 0:
        wordchoice = random.choice(wordList)
        print("you're hung!!")
        print("word was " + wordchoice)
        print("you made " + str(len(lettersGuessed)) + " guesses with " + str(missedletters) + " misses")
        return False
    elif "_" not in hangmanWord:
        print("you guessed the word: " + hangmanWord)
        print("you made " + str(len(lettersGuessed)) + " guesses with " + str(missedletters) + " misses")
        return True


if __name__ == "__main__":
    '''
    Running Hangman.py should start the game, which is done by calling runGame, therefore, we have provided you this code below.
    '''
    won = 0
    lost = 0

    while True:
        playgame = runGame('lowerwords.txt')
        playagain = input("Do you want to play again? y or n> ")
        if playgame == True:
            won += 1
        elif playgame == False:
            lost += 1
        if playagain == "n":
            print("You won " + str(won) + " game(s) and lost " + str(lost))
            break



