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




def getWord(words, length):
    '''
    Selects the secret word that the user must guess. 
    This is done by randomly selecting a word from words that is of length length.
    '''

    wordlist = []
    for item in words:
        if len(item) == length:
            wordlist.append(item)
    randomindexnumber = random.randint(0, len(wordlist) - 1)
    randomword = wordlist[randomindexnumber]
    return randomword



def createDisplayString(lettersGuessed, missesLeft, hangmanWord):
    '''
    Creates the string that will be displayed to the user, using the information in the parameters.
    '''
    lettersguessedstring = ""
    hangmanwordstring = ""
    for item in sorted(lettersGuessed):
        lettersguessedstring += item + " "

    for item in hangmanWord:
        hangmanwordstring += item + " "

    return "letters you've guessed: " + str(lettersguessedstring)  + "\nmisses remaining = " + str(missesLeft) +  "\n" + str(hangmanwordstring) +  "\n"





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



def updateHangmanWord(guessedLetter, secretWord, hangmanWord):
    '''
    Updates hangmanWord according to whether guessedLetter is in secretWord and where in secretWord guessedLetter is in.
    '''
    letterindex = 0
    if guessedLetter in secretWord:
        for item in secretWord:
            if item == guessedLetter:
                hangmanWord[letterindex] = item
            letterindex +=1
        return hangmanWord
    else:
        return hangmanWord



def processUserGuess(guessedLetter, secretWord, hangmanWord, missesLeft):
    '''
    Uses the information in the parameters to update the user's progress in the hangman game.
    '''

    newhangmanword = updateHangmanWord(guessedLetter, secretWord, hangmanWord)
    if guessedLetter not in secretWord:
        missesLeft -= 1
        userguess = False
    else:
        userguess = True
    return [newhangmanword, missesLeft, userguess]



def runGame(filename):
    '''
    This function sets up the game, runs each round, and prints a final message on whether or not the user won.
    True is returned if the user won the game. If the user lost the game, False is returned.
    '''
    file = open(filename, "r")
    wordsClean = [w.strip() for w in file.read().split()]
    words = wordsClean
    file.close()

    length = random.randint(5, 10)

    missesLeft = handleUserInputDifficulty()
    secretWord = getWord(words, length)

    hangmanWord = []
    lengthofword = len(secretWord)
    for item in range(lengthofword):
        hangmanWord.append("_")

    missedletters = 0
    lettersGuessed = []
    while "_" in hangmanWord and missesLeft != 0:
        displayString = createDisplayString(lettersGuessed, missesLeft, hangmanWord)
        guessedLetter = handleUserInputLetterGuess(lettersGuessed, displayString)
        lettersGuessed.append(guessedLetter)


        hangmanWord = updateHangmanWord(guessedLetter, secretWord, hangmanWord)
        if guessedLetter not in secretWord:
            missesLeft -= 1
            missedletters += 1
        correctorincorrect = processUserGuess(guessedLetter, secretWord, hangmanWord, missesLeft)
        if correctorincorrect == False:
            print("you missed: " + str(guessedLetter) + " not in word")


    if missesLeft == 0:
        print("you're hung!!")
        print("word is " + secretWord)
        print("you made " + str(len(lettersGuessed)) + " guesses with " + str(missedletters) + " misses")
        return False
    elif "_" not in hangmanWord:
        print("you guessed the word: "  + secretWord)
        print("you made " + str(len(lettersGuessed)) + " guesses with " + str(missedletters)  + " misses")
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
            won +=1
        elif playgame == False:
            lost +=1
        if playagain == "n":
            print("You won " + str(won) + " game(s) and lost " + str(lost))
            break



