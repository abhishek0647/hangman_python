# 
# Hangman game by Abhishek Kumar
#

# -----------------------------------

import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    secretWordLength = len(secretWord)
    correctGuesses = 0
    for letter in secretWord:
        if letter in lettersGuessed:
            correctGuesses += 1
    if correctGuesses == secretWordLength:
        return True
    else:
        return False



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    correctLetterGuessesList = ['_ ',] * len(secretWord)
    correctLetterGuessesString = ''
    for eachLetter in range(len(lettersGuessed)):
        for rightLetter in range(len(secretWord)):
            if lettersGuessed[eachLetter] == secretWord[rightLetter]:
                correctLetterGuessesList[rightLetter] = lettersGuessed[eachLetter] + ' '
    for each in range(len(correctLetterGuessesList)):
        correctLetterGuessesString = correctLetterGuessesString + correctLetterGuessesList[each]
    return correctLetterGuessesString



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    import string
    availLettersList = list(string.ascii_lowercase)
    availLettersString = ''
    for usedLetter in range(len(lettersGuessed)):
        for eachLetter in range(len(availLettersList)):
            if lettersGuessed[usedLetter] == availLettersList[eachLetter]:
                availLettersList.pop(eachLetter)
                break
    for each in range(len(availLettersList)):
        availLettersString = availLettersString + availLettersList[each]
    return availLettersString


def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.
    '''
    nguess = 8                                
    lettersGuessed = []
    result = ''

    print('Welcome to the game Hangman!') 
    print ('I am thinking of a word that is ' + str(len(secretWord)) + ' letters long.') 
    print('----------') 

    while nguess > 0: 
        print('You have ' + str(nguess) + ' guesses left') 
        print('Available Letters: ' + getAvailableLetters(lettersGuessed)) 
        G = raw_input('Please guess a letter:')
        if G.lower() in getAvailableLetters(lettersGuessed):
            lettersGuessed.append(G.lower())
            result += G.lower()
            if G.lower() in secretWord:
                getGuessedWord(secretWord, lettersGuessed)
                print('Good guess: ' + getGuessedWord(secretWord, lettersGuessed))
                print('----------')
                if isWordGuessed(secretWord, lettersGuessed):
                    print('Congratulations, you won!')
                    break
            else: 
                print('Oops! That letter is not in my word: ' + getGuessedWord(secretWord, lettersGuessed))
                print('----------')
                nguess -= 1
        else: 
            print("Oops! You've already guessed that letter: " + getGuessedWord(secretWord, lettersGuessed))
            print('----------') 
    
    if nguess == 0:
        print('Sorry, you ran out of guesses. The word was ' + str(secretWord) + '.')







secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
