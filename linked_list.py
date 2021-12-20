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

    def insert(self, value, index=0):
        if index < 0:
            raise IndexError("Please provide a non-negative index")
        elif index == 0:
            inserted_element = LinkedListElement(value, self.head)
            self.head = inserted_element
            return
        else:
            current_index = 0
            current_element = self.head
            while current_index < index - 1 and current_element:
                current_element = current_element.next
                current_index += 1
            if not current_element:
                raise IndexError(f"Index out of range, maximum index to insert to: {current_index}")
            else:
                inserted_element = LinkedListElement(value, current_element.next)
                current_element.next = inserted_element

    def insert_after_element(self, inserted_value, after_value):
        # Inserting after first occurrence of `after_value`, raises ValueError if not found
        current_element = self.head
        while current_element and current_element.value != after_value:
            current_element = current_element.next
        if current_element:
            current_element.next = LinkedListElement(inserted_value, current_element.next)
        else:
            raise ValueError(f"`after_value` {after_value} not found in LinkedList {str(self)}")

    def remove(self, index):
        if self.head is None:
            raise IndexError("LinkedList is empty; index out of range")
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
        # Removing first occurrence of element; doing nothing if not found
        if not self.head:
            return
        elif self.head.value == value:
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

    def append(self, value):
        if not self.head:
            self.head = LinkedListElement(value)
        else:
            current_element = self.head
            while current_element.next:
                current_element = current_element.next
            current_element.next = LinkedListElement(value)

    def pop(self):
        # Returns the last element and removes it from the list
        if not self.head:
            raise AttributeError("Cannot pop last element from empty list")
        elif not self.head.next:
            returned_value = self.head.value
            self.head = None
        else:
            current_element = self.head
            while current_element.next.next:
                current_element = current_element.next
            returned_value = current_element.next.value
            current_element.next = None
        return returned_value

    def sort(self):
        pass  # TODO hozzunk létre egy új listát

    @classmethod
    def factory(cls, *args):
        # To ease list creation in sample code
        if len(args) == 0:
            return cls()
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
