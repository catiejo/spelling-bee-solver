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

On the subject of dictionaries, the Spelling Bee puzzles are hand curated. Here's an email from NYT when I asked them about it...
> While words that are hyphenated, words that contain apostrophes and proper nouns are not part of our word list, every Spelling Bee puzzle is hand-curated to focus on relatively common words (with a couple tough ones here and there to keep it challenging). Occasionally we'll miss some common words and will add them in, but our puzzle editors ultimately draw from our internal lexicon and make the call for what's best with that day's puzzle.
>
> The key word here is 'common'. We certainly have dictionaries at our disposal, we just remove words from Spelling Bee that we believe not to be common enough, despite them being defined words, in order to maintain a level solving field for all of our solvers. We also try to avoid terms that are hyper-specific to any professional field, such as terms that might be familiar to, for example, a physician, ornithologist or geologist, but not to most people outside of that field.

I'm a nerd so I was curious what the differences were between my generated solutions and the hand-curated ones... and also if there are words my dictionary is missing. I cross check my list against the actual solution as follows:
1. Click on "Yesterday's Answers" and copy all of the words into a new json file 
2. JSON-ify them by putting the whole list in brackets, adding quotes around each word, and a comma after all words except the last (see gratiFy_solution.json). 
3. You can see the words that I found that weren't part of the NY Times solution by typing `spelling_bee.compare_solutions(solution, "your_solution_file.json)`.

Any words that weren't in the solution, and also any words that the solver didn't find, are printed to the console.

