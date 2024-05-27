with open('/root/workspace/github.com/Artimas831/bookbot/books/frankenstein.txt', 'r') as file:
	content = file.read()
	words = content.split()
	word_count = len(words)
	lowercase_content = content.lower()
	letters = list(lowercase_content)
	letters_dictionary = {}
	for letter in letters:
		if letter != '\n':
			if letter in letters_dictionary:
				letters_dictionary[letter] += 1
			else:
				letters_dictionary[letter] = 1
	Formatted_output = []
	sorted_letter_counts = sorted(letters_dictionary.items(), key=lambda item: item[1], reverse=True)
	for letter, count in sorted_letter_counts:
		if count > 1:
			Formatted_output.append(f"The character '{letter}' was used {count} times.")
		else:
			Formatted_output.append(f"The character '{letter}' was used {count} time.")
	print(content)
	print("--- Begin report of books/frankenstein.txt ---")
	print("There are", word_count, "words in this document.")
	print(" ")
	for entry in Formatted_output:
		print(entry)
	print("--- End Report ---")
