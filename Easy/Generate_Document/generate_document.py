def generateDocument(characters, document):
    
	c_dict = countFreq(characters)
	
	for d in document:
		if not d in c_dict:
			return False
		else:
			if document.count(d) > c_dict[d]:
				return False
			else:
				continue
    return True

def countFreq(string):
	char_dict = {}
	
	for c in string:
		if c not in char_dict:
			char_dict[c] = 1
		else:
			char_dict[c] += 1
			
	return char_dict
