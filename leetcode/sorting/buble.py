def bubble_sort(array):
    if array is None:
        return

    if not array:
        return array

    n = len(array)

    for x in range(n):
        for i in range(n - x - 1):
            if array[i] > array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]

    return array


def test_bubble_sort():
    assert [] == bubble_sort([])
    assert None == bubble_sort(None)
    assert [1, 2, 3, 4, 5] == bubble_sort([4, 3, 2, 1, 5])
    assert [0] == bubble_sort([0])
