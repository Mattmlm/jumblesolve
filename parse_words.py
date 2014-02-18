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

print prefix_tree('words_smaller.txt')