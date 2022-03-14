def validateBstHelper(tree, min_value, max_value):
	if tree is None:
		return True
	
	if tree.value < min_value or tree.value >= max_value:
		return False
	
	is_left_valid = validateBstHelper(tree.left, min_value, tree.value)
	is_right_valid = validateBstHelper(tree.right, tree.value, max_value)
	
	return is_left_valid and is_right_valid
