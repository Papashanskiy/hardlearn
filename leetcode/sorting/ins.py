def insertion_sort(array):
    if not array:
        return array

    for i in range(1, len(array)):
        curr = i
        while curr > 0 and array[curr-1] > array[curr]:
            array[curr], array[curr-1] = array[curr-1], array[curr]
            curr -= 1
    return array


def test_insertion_sort():
    assert [] == insertion_sort([])
    assert None == insertion_sort(None)
    assert [1, 2, 3, 4, 5] == insertion_sort([4, 3, 2, 1, 5])
    assert [0] == insertion_sort([0])
