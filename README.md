jumblesolve
===========

Using Python, solve the puzzle Jumble. http://en.wikipedia.org/wiki/Jumble

### To Run Jumble solve

Download jumble_solve2.py and words.txt.

#### Run the program in the terminal:

    python jumble_solve2.py word

#### For example:
input:

    python jumble_solve2.py dog

output:
    
    Length of original permutation is: 15
    ['go', 'god', 'do', 'dog', 'od']

#### Notes:
- jumblesolve.py is a program that runs efficiently for jumbled letters shorter than 4. Anything longer than that takes egregiously long to run.

#### Further potential optimizations:
- Reduce number of permutated words:
	- Eliminate words without vowels (except for a small number of exceptions)
- Create a more efficient data structure for the dictionary word list (words.txt). Currently it is organized into a dictionary with keys for each letter and lists of the words for each value.
    - Cost/benefits: More overhead time to make the structure, but the optimized data structure only needs to be created once.

#### TODO:
- Replace jumblesolve.py with jumble_solve2.py
- Write a more complete prefix_tree function.