def generateDocument(characters, document):
    char_dict = {}
	
	for c in characters:
		if c not in char_dict:
			char_dict[c] = 1
		else:
			char_dict[c] += 1
			
	for d in document:
		if not d in char_dict:
			return False
		else:
			if document.count(d) > char_dict[d]:
				return False
			else:
				continue
    return True
