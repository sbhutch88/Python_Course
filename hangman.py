def hangman(secretWord):
    print "\n" * 100
    secretWordLower = secretWord.lower()
    def getGuessedWord(secretWordLower,lettersGuessed):
        i = 0
        guesses = '_'
        while i < len(list(secretWordLower)):
            if list(secretWordLower)[i] in lettersGuessed:
                guesses += list(secretWordLower)[i]
            else:
                guesses += '_'
            i = i+1
        return guesses[1:]
    def isWordGuessed(secretWordLower,lettersGuessed):
        i = 0
        correct = 0
        while i < len(list(secretWordLower)):
            if list(secretWordLower)[i] in lettersGuessed:
                correct += 1
            i = i+1
        if correct == len(list(secretWordLower)):
            return True
        else:
            return False
    def getAvailableLetters(lettersGuessed):
        import string
        allLetters = list(string.ascii_lowercase)
        i = 0
        j = 0
        fullLetters = '-'
        while i < len(list(lettersGuessed)):
            allLetters.remove(lettersGuessed[i])
            i = i+1
        while j < len(allLetters):
            fullLetters += allLetters[j]
            j += 1
        return fullLetters[1:]
    
    
    print 'Welcome to the game, Hangman!'
    print 'I am thinking of a word that is ' + str(len(secretWord)) + ' letters long'
    numGuesses = 8
    lettersGuessed = []
    currentGuess  = []
    
    while numGuesses > 0:
        availableLetters = getAvailableLetters(lettersGuessed)
        print '-------------'
        print 'You have '+ str(numGuesses)+' guesses left.'
        print 'Available Letters: '+ str(availableLetters)
        guess = raw_input('Please guess a letter: ')
        guessLower = guess.lower()
        
        if guessLower in list(secretWordLower):
            if guessLower in lettersGuessed:
                print 'Oops! You\'ve already guessed that letter: '+currentGuess
            else:
                lettersGuessed += guessLower
                currentGuess = getGuessedWord(secretWordLower,lettersGuessed)
                if currentGuess == secretWordLower:
                    print 'Good guess: '+currentGuess
                    print '-------------'
                    print 'Congratulations, you won!'
                    break
                else:
                    print 'Good guess: '+currentGuess
        else:
            if guessLower in lettersGuessed:
                print 'Oops! You\'ve already guessed that letter: '+currentGuess
            else:
                lettersGuessed += guessLower
                currentGuess = getGuessedWord(secretWordLower,lettersGuessed)
                print 'Oops! That letter is not in my word: '+currentGuess
                numGuesses -=1 #This will probably need to be deleted later.
                if numGuesses == 0:
                    print '-------------'
                    print 'Sorry, you ran out of guesses. The word was '+ secretWord+'.'
                    break