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