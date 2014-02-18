# jumble_solve2.py

import sys

def prefix_tree(filename):
	dictionary_tree = dict()
	fin = open(filename)
	for line in fin:
		word = line.strip()
		if word[0] in dictionary_tree.keys():
			updated_list = dictionary_tree[word[0]] + [word]
			dictionary_tree[word[0]] = updated_list
		else:
			dictionary_tree[word[0]] = [word]
	return dictionary_tree

def word_exists(test_word, dictionary_list):
	words_to_check = dictionary_list[test_word[0]]
	for word in words_to_check:
		if (word == test_word):
			return True
	return False

def jumble_solve(word_list):
	dict_list = prefix_tree('words.txt')
	updated_word_list = []
	for word in word_list:
		if word_exists(word, dict_list):
			updated_word_list.append(word)
	return updated_word_list

# Inputs:
#  - list type, word_list
#  - string, word
#  - list type, remaining_letters
def permute_words(word_list, word, remaining_letters):
	# Get the unique letters of the remaining_letters (prevent duplicates)
	unique_letters = set(remaining_letters)
	# print "unique_letters"
	# print unique_letters

	# Base case, last letter
	if len(remaining_letters) == 1:
		# Add only unique letters
		for letter in unique_letters:
			word_list.append(word + letter)

	# Recursive call
	else:
		for letter in unique_letters:
			# print "letter"
			# print letter
			# Updated parameters for recursive call
			new_word = word + letter
			# print "remaining_letters"
			# print remaining_letters
			x = remaining_letters.index(letter)
			new_remaining_letters = remaining_letters[:x] + remaining_letters[x+1:]
			# print "new_remaining_letters"
			# print new_remaining_letters
			# print "remaining_letters checking"
			# print remaining_letters

			word_list.append(new_word)
			permute_words(word_list, new_word, new_remaining_letters)
	return word_list

original_permutation = permute_words([], "", list(sys.argv[1]))
print "Length of original permutation is: " + str(len(original_permutation))
# print original_permutation
print jumble_solve(original_permutation)