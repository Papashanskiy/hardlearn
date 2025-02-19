def insertion_sort(array):
    pass


def test_insertion_sort():
    assert [] == insertion_sort([])
    assert None == insertion_sort(None)
    assert [1, 2, 3, 4, 5] == insertion_sort([4, 3, 2, 1, 5])
    assert [0] == insertion_sort([0])
