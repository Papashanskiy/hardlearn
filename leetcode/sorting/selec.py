def selec_sort(array):
    if not array:
        return array

    n = len(array)

    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if array[j] < array[min_index]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]

    print(array)
    return array


def test_bubble_sort():
    assert [] == selec_sort([])
    assert None == selec_sort(None)
    assert [1, 2, 3, 4, 5] == selec_sort([4, 3, 2, 1, 5])
    assert [0] == selec_sort([0])
