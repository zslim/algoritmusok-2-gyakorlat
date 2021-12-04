class LinkedListElement:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next


class LinkedList:
	def __init__(self, head: LinkedListElement = None):
		self.head = head

	def __repr__(self):
		string = "["
		current = self.head
		while current:
			string += str(current.value) + ", " if current.next else str(current.value)
			current = current.next
		string += "]"
		return string

	def traverse(self, func):
		current = self.head
		while current:
			func(current.value)
			current = current.next

	def search(self, element):
		current = self.head
		index = 0
		while current:
			if current.value == element:
				return index
			else:
				index += 1
				current = current.next
		return None

	def insert(self, index):
		pass  # TODO

	def insert_after_element(self, element):
		pass  # TODO

	def remove(self, index):
		if index == 0:
			self.head = self.head.next
		else:
			previous = self.head
			current = self.head.next
			current_index = 1
			while current:
				if current_index == index:
					previous.next = current.next
				else:
					index += 1
					previous = current
					current = current.next
		# TODO

	def remove_element(self, value):
		pass  # TODO

	def append(self, value):
		pass  # TODO

	def pop(self):
		pass  # TODO

	def sort(self):
		pass  # TODO hozzunk létre egy új listát
