class TreeElement:
	def __init__(self, value, left=None, right=None):
		self.value = value
		self.left = left
		self.right = right

	def __repr__(self):
		return str(self.value)


class BinaryTree:
	def __init__(self, root: TreeElement = None):
		self.root = root

	def traverse_in_order(self, func, current_element):
		if current_element is not None:
			self.traverse_in_order(func, current_element.left)
			func(current_element)
			self.traverse_in_order(func, current_element.right)

	def traverse_post_order(self, func, current_element):
		if current_element is not None:
			self.traverse_in_order(func, current_element.left)
			self.traverse_in_order(func, current_element.right)
			func(current_element)

	def traverse_pre_order(self, func, current_element):
		if current_element is not None:
			func(current_element)
			self.traverse_in_order(func, current_element.left)
			self.traverse_in_order(func, current_element.right)

	@classmethod
	def factory(cls, *args):
		def create_recursive(low, high):
			if low <= high:
				middle = (low + high) // 2
				return TreeElement(args[middle], create_recursive(low, middle - 1), create_recursive(middle + 1, high))
			else:
				return None
		return cls(create_recursive(0, len(args) - 1))


if __name__ == '__main__':
	tree = BinaryTree.factory(1, 2, 3, 4, 5, 6, 7, 8)
	print("\nIn order")
	tree.traverse_in_order(print, tree.root)
	print("\nPost order")
	tree.traverse_post_order(print, tree.root)
	print("\nPre-order")
	tree.traverse_pre_order(print, tree.root)
