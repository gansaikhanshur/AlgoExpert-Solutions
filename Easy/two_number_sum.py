def twoNumberSum(array, targetSum):
	output = []
    for i in enumerate(array):
		for j in enumerate(array):
			if i[0] != j[0]:
				if i[1] + j[1] == targetSum:
					return [i[1], j[1]]
	return output
