import pytest

from linked_list import LinkedList


@pytest.mark.parametrize(["numbers", "search_value", "expected_index"], [
    ((1, 2, 3, 4, 5), 2, 1), ((1, 2, 3, 4), 5, None), ((1, 2, 3, 1, 2), 1, 0), ((1, 2, 3, 1, 2), 2, 1)
])
def test_search(numbers, search_value, expected_index):
    my_list = LinkedList.factory(*numbers)
    actual = my_list.search(search_value)
    assert actual == expected_index


@pytest.mark.parametrize(["numbers", "value", "index", "expected_numbers"], [
    ((1, 2, 3, 4), 5, 2, (1, 2, 5, 3, 4)), ((1, 2, 3, 4), 5, 0, (5, 1, 2, 3, 4))
])
def test_insert(numbers, value, index, expected_numbers):
    my_list = LinkedList.factory(*numbers)
    my_list.insert(value, index)
    expected = LinkedList.factory(*expected_numbers)
    assert my_list == expected


@pytest.mark.parametrize(["numbers", "index"], [
    ((1, 2, 3, 4), 5), ((1, 2, 3, 4), -1)
])
def test_insert_index_error(numbers, index):
    my_list = LinkedList.factory(*numbers)
    with pytest.raises(IndexError):
        my_list.insert(99999, index)


def test_insert_after_element():
    my_list = LinkedList.factory(1, 2, 3, 4, 5)
    my_list.insert_after_element(99, 4)
    expected = LinkedList.factory(1, 2, 3, 4, 99, 5)
    assert my_list == expected


def test_remove():
    my_list = LinkedList.factory(1, 2, 3, 4, 5)
    my_list.remove(1)
    expected = LinkedList.factory(1, 3, 4, 5)
    assert my_list == expected


@pytest.mark.parametrize(["numbers", "element", "expected_numbers"], [
    ((1, 2, 3, 4), 1, (2, 3, 4)), ((1, 2, 5, 1), 1, (2, 5, 1)),
    ((1, 2, 3, 4, 5), 3, (1, 2, 4, 5)), ((1, 2, 3, 2, 4), 2, (1, 3, 2, 4))
])
def test_remove_element(numbers, element, expected_numbers):
    my_list = LinkedList.factory(*numbers)
    my_list.remove_element(element)
    expected = LinkedList.factory(*expected_numbers)
    assert my_list == expected
