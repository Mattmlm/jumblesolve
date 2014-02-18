import sys

def word_exists(test_word):
	fin = open('words.txt')
	for line in fin:
		word = line.strip()
		if (word == test_word):
			return True
	return False

def word_exists_test(test_word):
	fin = open('words_smaller.txt')
	for line in fin:
		word = line.strip()
		if (word == test_word):
			return True
	return False

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


#######################################################
##### POTENTIAL OPTIMIZATIONS FOR PERMUTATIONS ########
#######################################################

# Check if vowel
# This checks for presence of a e i o u y
# NOTE: THIS CHECKS FOR Y AS WELL
def is_vowel(letter):
	if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u' or letter == 'y':
		return True
	else:
		return False

# Check for vowel
# NOTE: IF THERE IS A Y, THIS RETURNS TRUE
def contains_vowel(word):
	for letter in word:
		if is_vowel(letter):
			return True
	return False

# Check first four letters of word
def less_than_four_consonants(word):
	for x in range(0, 4):
		if is_vowel(word[x]):
			return True
	return False

# Optimization method
def strip_nonwords(word_list):
	updated_word_list = []
	for word in word_list:

		# # Keep only single letter words that are 'a' 'i' or 'o'
		# if len(word) == 1 and (word == 'a' or word == 'i' or word == 'o'):
		# 	print "Allowing one letter words"
		# 	updated_word_list.append(word)
		# # Length > 1
		# else:
		# 	# Check if word contains a vowel or y
		# 	# It's not a word if it doesn't contain a vowel or y
		# 	if contains_vowel(word):
		# 		if len(word) >= 4:
		# 			if less_than_four_consonants:
		# 				updated_word_list.append(word)
		# 		else:
		# 			updated_word_list.append(word)

		if word_exists(word):
			updated_word_list.append(word)

	return updated_word_list

original_permutation = permute_words([], "", list(sys.argv[1]))
print "Length of original permutation is: " + str(len(original_permutation))

optimized_list = strip_nonwords(original_permutation)
print "Length of optimized_list is: " + str(len(optimized_list))
print optimized_list
# print word_exists("crwth")
# print word_exists("cwm")
# print word_exists("tsk")
# print word_exists("qwerty")