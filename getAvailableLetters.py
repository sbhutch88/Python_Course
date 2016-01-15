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