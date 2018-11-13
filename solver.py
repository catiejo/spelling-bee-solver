# todo: use this file to process: https://github.com/dwyl/english-words

def getLetters(word):
    letters = ""
    for char in word:
        if char not in letters:
            letters += char
    return ''.join(sorted(letters))

def processDictionary(dictionary):
    dict_by_letters = {}
    for word in dictionary:
        letters_for_word = getLetters(word)
        if letters_for_word not in dict_by_letters:
            dict_by_letters[letters_for_word] = []
        dict_by_letters[letters_for_word].append(word)
    return dict_by_letters
