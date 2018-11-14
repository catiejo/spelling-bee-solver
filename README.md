# Spelling Bee Solver
A simple python script to solve the NY Times spelling bee puzzle. (www.nytimes.com/puzzles/spelling-bee)

## Quickstart
1. Download repository and extract it from teh zip file.
2. Open a terminal window, and navigate to the directory (e.g. `cd Downloads/spelling-bee-solver-master`)
3. start python by typing `python` into the terminal prompt (this app was written using python 2.7, so it should work on a default mac installation)
4. import the module with `import spelling_bee`, and you're all set!

## How to use the script
The `solve()` function takes a string of any length, treating lowercase letters as normal letters, and uppercase letters as mandatory (the yellow middle letter in the NY Times puzzle).
* `spelling_bee.solve("inkblOt")`
* `spelling_bee.solve("inkblOt", dictionary_path="../path/to/your/dictionary")` *(default: dictionary.json included in repo)*
* `spelling_bee.solve("inkblOt", minimum_word_length=2)` *(default: 4)*

(you can also assign the solution to a local variable: `solution = spelling_bee.solve("inkblOt")`)

## Notes
I'm using a scrabble json dictionary I found [here](https://github.com/benjamincrom/scrabble/blob/master/scrabble/dictionary.json), but you can easily sub in your own dictionary. However, I'm expecting a file format of `["word1", "word2", ..., "wordN"]`, so modify the `json_to_list()` function if you want to use something else.

On the subject of dictionaries, I have no clue what dictionary the actual puzzle is using, so there are usually a number of words that my solver finds that aren't actually solutions to the NY Times puzzle. I'm a nerd so I was curious what those words were... so I cross check my list against the actual solution as follows:
1. Click on "Yesterday's Answers" and copy all of the words into a new json file 
2. JSON-ify them by putting the whole list in brackets, adding quotes around each word, and a comma after all words except the last (see gratiFy_solution.json). 
3. You can see the words that I found that weren't part of the NY Times solution by typing `spelling_bee.compare_solutions(solution, "your_solution_file.json)`.

