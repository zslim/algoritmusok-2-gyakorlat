class TreeElement:
	def __init__(self, value, left=None, right=None):
		self.value = value
		self.left = left
		self.right = right


class BinaryTree:
	def __init__(self, root: TreeElement):
		self.root = root
