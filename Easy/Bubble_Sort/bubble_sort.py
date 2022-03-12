def bubbleSort(array):
	is_sorted = False
	
	while not is_sorted:
		is_sorted = True
		
		for idx in range(len(array) - 1):
			if array[idx] > array[idx + 1]:
				array[idx + 1], array[idx] = array[idx], array[idx + 1]
				is_sorted = False
	
    return array
