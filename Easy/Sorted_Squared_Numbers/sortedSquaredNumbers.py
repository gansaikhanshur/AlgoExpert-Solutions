def sortedSquaredArray(array):
    
	output = []
	
    # O(N)T, O(N)S.
	for num in array:
		square = num * num
		output.append(square)
		
	# Additional sorting needed because of negative numbers
	output.sort()
			
    return output
