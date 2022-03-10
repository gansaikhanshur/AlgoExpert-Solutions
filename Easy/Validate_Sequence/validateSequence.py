def isValidSubsequence(array, sequence):
	
	is_valid = False
	
	# O(N)T, O(1)
	for entry in array:
		if entry == sequence[0]:
			sequence.pop(0)
		
		if len(sequence) == 0:
			return True
	
	
	return is_valid
