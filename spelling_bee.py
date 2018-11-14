import json

# returns a string of the unique, alphabetized letters in the given word
def get_letters(word):
    letters = ""
    for char in word:
        if char not in letters:
            letters += char
    return ''.join(sorted(letters))

# json files must be in form ["word1", "word2", "word3"] (see dictionary.json)
def json_to_list(filepath):
    with open(filepath) as f:
        dict = json.load(f)
    return [word.encode("utf-8") for word in dict]

# generated_solution is the solution returned by the solve() method
def compare_solutions(generated_solution, path_to_actual_solution):
    actual_solution = set(json_to_list(path_to_actual_solution))
    generated_solution = set(generated_solution)
    return list(generated_solution.difference(actual_solution))

# Generates a dict where the key is a string of the unique, alphabetized letters
# in the word, and the key is the list of all words using that letterself. For
# example, an entry could be {"bo": ["boob", "booboo"]}
def process_dictionary(path_to_dictionary, min_word_length):
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

# Goes through the dictionary and removes entries that either (1) contain letters
# that aren't in the spelling bee puzzle or (2) don't contain the mandatory letters.
def prune_dictionary(dictionary_dict, spelling_bee):
    spelling_bee_letters = set([letter.lower() for letter in list(spelling_bee)])
    mandatory_letters = set([letter.lower() for letter in list(spelling_bee) if letter.isupper()])
    for key in dictionary_dict.keys():
        key_letters = set(list(key))
        if not key_letters.issubset(spelling_bee_letters) or not mandatory_letters.issubset(key_letters):
            del dictionary_dict[key]

# e.g. solve("inkOblt"), solve("inkOblt", dictionary_path="dictionary.json")
def solve(spelling_bee, **optional_parameters):
    dictionary_path = 'dictionary.json'
    min_word_length = 4
    if 'dictionary_path' in optional_parameters:
        dictionary_path = optional_parameters['dictionary_path']
    if 'min_word_length' in optional_parameters:
        min_word_length = optional_parameters['min_word_length']
    dictionary_dict = process_dictionary(dictionary_path, min_word_length)
    prune_dictionary(dictionary_dict, spelling_bee)
    words_in_solution = []
    # dictionary_dict.values() is a list of lists of words.
    for words in list(dictionary_dict.values()):
        for word in words:
            words_in_solution.append(word)
    return words_in_solution
