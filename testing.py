fin = open('words.txt')
starts_with_a_words = 0
for line in fin:
    word = line.strip()
    def starts_with_a(word):
        global starts_with_a_words
        if word[0] == 'b':
            # print word
            starts_with_a_words +=1
    starts_with_a(word)
print "Words starting with 'a' as percentage = " + str(((starts_with_a_words/113809.0)*100))
            
    
test_letters = "dog"
def word_exists(test_word):
	fin = open('words.txt')
	for line in fin:
		word = line.strip()
		if (word == test_word):
			return True
	return False

word_exists("dog")

def permute(word_list, word, remaining_letters):
	# print "Starting permute..."
	# print "word:"
	# print word
	# print "remaining_letters:"
	# print remaining_letters
	if len(remaining_letters) == 0:
		# print("append last combination")
		word_list.append(word)
	else:
		# print "word_list:"
		# print word_list
		for x in range(0, len(remaining_letters)):
			# print "Remaining_letters:"
			# print remaining_letters
			new_word = word + remaining_letters[x]
			new_remaining_letters = remaining_letters[:x] + remaining_letters[x+1:]
			if len(word) > 1:
				word_list.append(word)
			permute(word_list, new_word, new_remaining_letters)
		# print word_list
		return word_list

finalwordlist = permute([], "", "god")
print "final word list:"
print finalwordlist

def generate_permutations(word):
	permutations = []

def solve_jumble(jumbled_letters):
	permutations = permute([], "", jumbled_letters)
	solution = []
	for word in permutations:
		if word_exists(word):
			solution.append(word)
	return solution

test_letters = "large"

print "permutations are: "
print permute([], "", test_letters)

print "solution is: "
print solve_jumble(test_letters)