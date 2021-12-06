def twoNumberSum(array, targetSum):
    #Loop through the main array
    for i in enumerate(array):
        #Second loop to step to the right direction
		for j in enumerate(array):
            #make sure that we're not adding the same index twice
			if i[0] != j[0]:
				if i[1] + j[1] == targetSum:
					return [i[1], j[1]]
	return []
