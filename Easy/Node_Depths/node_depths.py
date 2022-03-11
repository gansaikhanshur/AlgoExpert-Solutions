def nodeDepths(root):
    output = 0
	queue = [{"node": root, "level": 0}]
	
	while len(queue) > 0:
		node_info = queue.pop()
		curr_node, curr_level = node_info["node"], node_info["level"]

		if curr_node is None:
			continue
		
		output += curr_level
		
		queue.append({"node": curr_node.left, "level": curr_level + 1})
		queue.append({"node": curr_node.right, "level": curr_level + 1})
		
			
	return output


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
