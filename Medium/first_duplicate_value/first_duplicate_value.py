def firstDuplicateValue(array):
	seen = []
    for i in array:
		if i in seen:
			return i
		else:
			seen.append(i)
			
	return -1
