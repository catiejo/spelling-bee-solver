import json

min_word_length = 4

def get_letters(word):
    letters = ""
    for char in word:
        if char not in letters:
            letters += char
    return ''.join(sorted(letters))

def json_to_list(filepath):
    with open(filepath) as f:
        dict = json.load(f)
    dict_list = list(dict.keys())
    return [word.encode("utf-8") for word in dict_list]

def process_dictionary(path_to_dictionary):
    dictionary = json_to_list(path_to_dictionary)
    dict_by_letters = {}
    for word in dictionary:
        if len(word) < min_word_length:
            continue
        letters_for_word = get_letters(word)
        if letters_for_word not in dict_by_letters:
            dict_by_letters[letters_for_word] = []
        dict_by_letters[letters_for_word].append(word)
    return dict_by_letters

def prune_words(words_by_letters, spelling_bee):
    mandatory_letters = set([letter.lower() for letter in list(spelling_bee) if letter.isupper()])
    other_letters = set([letter for letter in list(spelling_bee) if letter.islower()])
    for key in words_by_letters.keys():
        key_as_set = set(list(key))
        # each word has to contain all mandatory letters
        if not mandatory_letters.issubset(key_as_set):
            del words_by_letters[key]
        else:
            # subtracts mandatory letters from the key.
            key_other_letters = key_as_set.difference(mandatory_letters)
            if not key_other_letters.issubset(other_letters):
                del words_by_letters[key]
    return words_by_letters

# brute force appoach
def solve(spelling_bee, path_to_dictionary):
    dictionary = process_dictionary(path_to_dictionary)
    pruned_dictionary = prune_words(dictionary, spelling_bee)
    valid_words = []
    for word_list in list(dictionary.values()):
        for word in word_list:
            valid_words.append(word)
    return valid_words
