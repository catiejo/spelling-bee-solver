import json

# json files must be in form ["word1", "word2", "word3"] (see dictionary.json)
def json_to_list(filepath):
    with open(filepath) as f:
        dict = json.load(f)
    return [word.lower().encode("utf-8") for word in dict]

# generated_solution is the solution returned by the solve() method
def compare_solutions(generated_solution, path_to_actual_solution):
    actual_solution = set(json_to_list(path_to_actual_solution))
    generated_solution = set(generated_solution)
    print("Words the solver found that aren't in the solution:")
    print list(generated_solution.difference(actual_solution))
    print ("Words that are in the solution that the solver didn't find:")
    print list(actual_solution.difference(generated_solution))

# this goes through each word in the dictionary and checks if it belongs in the solution
def get_words_in_solution(spelling_bee, dictionary, min_letters):
    bee_letters = set([letter.lower() for letter in list(spelling_bee)])
    required_letters = set([letter.lower() for letter in list(spelling_bee) if letter.isupper()])
    solution = []
    for word in dictionary:
        if len(word) < min_letters:
            continue
        letters = set([list(word)])
        if letters.issubset(bee_letters) and required_letters.issubset(letters):
            solution.append(word)
    return solution

# e.g. solve("inkOblt"), solve("inkOblt", dict_path="dictionary.json")
def solve(spelling_bee, **optional_parameters):
    dictionary_path = optional_parameters['dict_path'] if ('dict_path' in optional_parameters) else 'dictionary.json'
    min_word_length = optional_parameters['min_letters'] if ('min_letters' in optional_parameters) else 4
    dictionary = json_to_list(dictionary_path)
    return get_words_in_solution(spelling_bee, dictionary, min_word_length)
