
def words(phrase):
	#  separate the words and add each word to a list called separated_words
	separated_words = phrase.split()

	#defines an empty dictionary that will store separated words 
	words_temporary_storage = {}

    #extract each word from the list
	for word in separated_words:

		#check if the word is stored in our temporary storage .
		if word in words_temporary_storage:
			continue
		else:
			#If the word is not in our temporary storage , then add it
			words_temporary_storage[word] = separated_words.count(word)
	
	#define final output dictionary to store occurances of a word
	final_output = {}

    #get each word from the words_temporary_storage dictionary
	for item in words_temporary_storage.items():
		#check the word occurance
		if item[0].isdigit():
			final_output[int(item[0])] = item[1]
		else:
			final_output[item[0]] = item[1]

	return final_output 