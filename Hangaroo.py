# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 11:42:15 2019

@author: PL SERIES
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 11:41:32 2019

@author: PL SERIES
"""


def isWordGuessed(secretWord,lettersGuessed):      
    for x in secretWord:
        if x in lettersGuessed:
            return ("true")
        else:
            return ("false")
def getGuessedWord(secretWord,lettersGuessed):
    word = ''
    for x in secretWord:
        if x in lettersGuessed:
            word += x
        else:
            word += '_ '
    return word
def getAvailableLetters(lettersGuessed):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 

                'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for letter in lettersGuessed:
        alphabet.remove(letter) 
    return ' '.join(alphabet)
secretWord = "secret"
def Hangaroo(secretWord):
    L = str(len(secretWord))
    mistakes = 7
    answer = str
    wordGuess = False
    lettersGuessed = []
    print ('Lets play a game! Lets play Hangaroo')
    print ("You have to guess a word that is " + L, "letters long.")
    print ('-----------')
    while mistakes > 0 and mistakes <= 7 and wordGuess is False:
         if secretWord == getGuessedWord(secretWord, lettersGuessed):
             wordGuess= True
             break
         print ('You have ' + str(mistakes), 'guesses left.')
         print ('Available letters: ')
         print(getAvailableLetters(lettersGuessed))
         answer = input('Please guess a letter: ').lower()
         if answer in secretWord:
             if answer in lettersGuessed:
                print ("Ouch! You already guessed that letter. Please try again!: ")
                print (getGuessedWord(secretWord, lettersGuessed))
                print ('------------')
             else:
                lettersGuessed.append(answer)
                print ('Good guess: ') 
                print (getGuessedWord(secretWord, lettersGuessed))
                print ('------------')
         else:
             if answer in lettersGuessed:
                print ("Ouch! You already guessed that letter. Please try again: ") 
                print (getGuessedWord(secretWord, lettersGuessed))
                print ('------------')
             else:
                lettersGuessed.append(answer)
                mistakes -= 1
                print ('Ouch! That letter is not in my word: ') 
                print (getGuessedWord(secretWord, lettersGuessed))
                print ('------------')
    if wordGuess == True:
        return 'Congratulations, you won!'
    elif mistakes == 0:
        print ('You ran out of guesses. The word was ') 
        print (secretWord)

