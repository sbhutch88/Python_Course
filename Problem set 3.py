secretWord = 'apple'
lettersGuessed = ['e','i','k','p','r','s','l']

def isWordGuessed(secretWord,lettersGuessed):
    i = 0
    correct = 0
    while i < len(list(secretWord)):
        if list(secretWord)[i] in lettersGuessed:
            correct += 1
        i = i+1
    if correct == len(list(secretWord)):
        return True
    else:
        return False
        
print isWordGuessed(secretWord,lettersGuessed)


secretWord = 'apple'
letterGuessed = ['e','i','k','p','r','s']
guesses = '_'

def getGuessedWord(secretWord,lettersGuessed):
    i = 0
    guesses = '_'
    while i < len(list(secretWord)):
        if list(secretWord)[i] in lettersGuessed:
            guesses += list(secretWord)[i]
        else:
            guesses += '_'
        i = i+1
    return guesses[1:]
    

