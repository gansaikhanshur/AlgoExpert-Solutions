def invertBinaryTree(tree):
    queue = [tree]
	
	while len(queue) > 0:
		curr_node = queue.pop(0)
		if curr_node is None:
			continue
		curr_node.left, curr_node.right = curr_node.right, curr_node.left
		queue.append(curr_node.left)
		queue.append(curr_node.right)
		
	return tree


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
