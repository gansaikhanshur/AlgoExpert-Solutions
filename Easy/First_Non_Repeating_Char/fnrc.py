def firstNonRepeatingCharacter(string):
	
	seen = []
	non_repeating = []
	
	for char in string:
		if char not in seen:
			seen.append(char)
			non_repeating.append(char)
		elif char in seen and char in non_repeating:
			non_repeating.remove(char)
			
	if len(non_repeating) > 0:
		return string.index(non_repeating[0])
	
	return -1
