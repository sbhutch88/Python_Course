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