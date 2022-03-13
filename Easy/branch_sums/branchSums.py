# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
		
def branchSums(root):
	sums = []
	
	calculateBranchSum(root, 0, sums)
	
    return sums

def calculateBranchSum(node, current_sum, sums):
	if node is None:
		return
	
	new_current_sum = current_sum + node.value
	
	if node.left is None and node.right is None:
		sums.append(new_current_sum)
		
	calculateBranchSum(node.left, new_current_sum, sums) 
	calculateBranchSum(node.right, new_current_sum, sums)
	
	return sums
