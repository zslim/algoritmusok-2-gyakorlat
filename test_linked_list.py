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
    ((1, 2, 3, 4), 5, 2, (1, 2, 5, 3, 4)), ((1, 2, 3, 4), 5, 0, (5, 1, 2, 3, 4)),
    ((1, 2, 3, 4), 1, 2.8, (1, 2, 3, 1, 4)), ((1, 2, 3, 4), 5, 4, (1, 2, 3, 4, 5))
])
def test_insert(numbers, value, index, expected_numbers):
    my_list = LinkedList.factory(*numbers)
    my_list.insert(value, index)
    expected = LinkedList.factory(*expected_numbers)
    assert my_list == expected


@ pytest.mark.parametrize(["numbers", "inserted", "expected_numbers"], [
    ((1, 2, 3, 4), 9, (9, 1, 2, 3, 4)), ((1,), 0, (0, 1))
])
def test_insert_default_param(numbers, inserted, expected_numbers):
    my_list = LinkedList.factory(*numbers)
    my_list.insert(inserted)
    expected = LinkedList.factory(*expected_numbers)
    assert my_list == expected


@pytest.mark.parametrize(["numbers", "index"], [
    ((1, 2, 3, 4), 5), ((1, 2, 3, 4), -1)
])
def test_insert_index_error(numbers, index):
    my_list = LinkedList.factory(*numbers)
    with pytest.raises(IndexError):
        my_list.insert(99999, index)


@pytest.mark.parametrize(["numbers", "inserted", "after", "expected_numbers"], [
    ((1, 2, 3, 4), 9, 1, (1, 9, 2, 3, 4)), ((1, 2, 1, 4, 5), 9, 1, (1, 9, 2, 1, 4, 5)),
    ((4,), 9, 4, (4, 9)), ((1, 2, 3, 4, 4, 4), 9, 4, (1, 2, 3, 4, 9, 4, 4))
])
def test_insert_after_element(numbers, inserted, after, expected_numbers):
    my_list = LinkedList.factory(*numbers)
    my_list.insert_after_element(inserted, after)
    expected = LinkedList.factory(*expected_numbers)
    assert my_list == expected


@pytest.mark.parametrize(["numbers", "after"], [
    ((1, 2, 3, 4), 8), ((1,), 5)
])
def test_insert_after_element_value_error(numbers, after):
    inserted_value = 9999
    my_list = LinkedList.factory(*numbers)
    with pytest.raises(ValueError):
        my_list.insert_after_element(inserted_value, after)


@pytest.mark.parametrize(["numbers", "removed_index", "expected_numbers"], [
    ((1, 2, 3, 4, 5), 0, (2, 3, 4, 5)), ((1, 2, 3, 4, 5), 4, (1, 2, 3, 4))
])
def test_remove(numbers, removed_index, expected_numbers):
    my_list = LinkedList.factory(*numbers)
    my_list.remove(removed_index)
    expected = LinkedList.factory(*expected_numbers)
    assert my_list == expected


@pytest.mark.parametrize(["numbers", "removed_index"], [
    ((1, 2, 3, 4), 5), ((1, 2, 3, 4, 5), -2), ((), 0), ((), 1)
])
def test_remove_index_error(numbers, removed_index):
    my_list = LinkedList.factory(*numbers)
    with pytest.raises(IndexError):
        my_list.remove(removed_index)


@pytest.mark.parametrize(["numbers", "value", "expected_numbers"], [
    ((1, 2, 3, 4), 1, (2, 3, 4)), ((1, 2, 5, 1), 1, (2, 5, 1)),
    ((1, 2, 3, 4, 5), 3, (1, 2, 4, 5)), ((1, 2, 3, 2, 4), 2, (1, 3, 2, 4)),
    ((), 1, ()), ((1, 2, 3, 4), 9, (1, 2, 3, 4))
])
def test_remove_element(numbers, value, expected_numbers):
    my_list = LinkedList.factory(*numbers)
    my_list.remove_element(value)
    expected = LinkedList.factory(*expected_numbers)
    assert my_list == expected
