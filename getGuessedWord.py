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