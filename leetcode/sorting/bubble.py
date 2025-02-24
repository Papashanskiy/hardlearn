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


def bubble_sort_2(array):
    if not array:
        return array

    n = len(array)
    for i in range(n):
        for j in range(n - i - 1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]

    return array


def bubble_sort_3(array):
    if not array:
        return array

    n = len(array)

    has_swapped = True
    while has_swapped:
        has_swapped = False
        for i in range(n - 1):
            if array[i] > array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
                has_swapped = True

    return array


def test_bubble_sort():
    assert [] == bubble_sort_2([])
    assert None == bubble_sort_2(None)
    assert [1, 2, 3, 4, 5] == bubble_sort_2([4, 3, 2, 1, 5])
    assert [0] == bubble_sort_2([0])
