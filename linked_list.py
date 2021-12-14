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

    def __eq__(self, other):
        current_self = self.head
        current_other = other.head
        while current_self or current_other:
            if not current_self or not current_other or current_self.value != current_other.value:
                return False
            current_self = current_self.next
            current_other = current_other.next
        return True

    def traverse(self, func):
        current = self.head
        while current:
            func(current.value)
            current = current.next

    def search(self, value):
        # Returning the index of the first occurrence of `value`, or None if not found
        current = self.head
        index = 0
        while current:
            if current.value == value:
                return index
            else:
                index += 1
                current = current.next
        return None

    def insert(self, value, index=0):  # TODO: clean this up
        # Raises IndexError if index is out of range (greater than the number of elements before inserting)
        if index < 0:
            raise ValueError("Please provide a non-negative index")
        current_index = 0
        current_element = self.head
        while current_index < index - 1:
            if not current_element:
                raise IndexError(f"Index out of range, maximum index to insert to: {current_index}")
            current_element = current_element.next
            current_index += 1
        inserted_element = LinkedListElement(value, current_element.next)
        current_element.next = inserted_element

    def insert_after_element(self, inserted_value, after_value):
        # Inserting after first occurrence of `after_value`, or at the end of the list
        current_element = self.head
        while current_element and current_element.value != after_value:
            current_element = current_element.next
        current_element.next = LinkedListElement(inserted_value, current_element.next)

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
                    return
                else:
                    current_index += 1
                    previous = current
                    current = current.next
            raise IndexError("LinkedList index out of range")

    def remove_element(self, value):
        # Removing first occurrence of element or raising ValueError if not found
        if self.head.value == value:
            self.head = self.head.next
        else:
            previous_element = self.head
            current_element = self.head.next
            while current_element:
                if current_element.value == value:
                    previous_element.next = current_element.next
                    return
                previous_element = current_element
                current_element = current_element.next
            raise ValueError("Could not remove element because it could not be found")

    def append(self, value):
        pass  # TODO

    def pop(self):
        pass  # TODO

    def sort(self):
        pass  # TODO hozzunk létre egy új listát

    @classmethod
    def factory(cls, *args):
        # To ease list creation in sample code
        head = LinkedListElement(args[-1])
        for i in range(len(args) - 1, 0, -1):
            next = head
            head = LinkedListElement(args[i - 1], next)
        return cls(head)

    @classmethod
    def factory_recursive(cls, *args):
        # For fun
        def create_recursive(index):
            if index == len(args) - 1:
                return LinkedListElement(args[index])
            else:
                return LinkedListElement(args[index], create_recursive(index + 1))
        return cls(create_recursive(0))


if __name__ == '__main__':
    lista = LinkedList.factory(1, 2, 3, 4, 5, 6)
    print(f"iteratívan létrehozott lista: {lista}")
    lista_rec = LinkedList.factory_recursive(1, 2, 3, 4, 5, 6)
    print(f"rekurzívan létrehozott lista: {lista_rec}")
