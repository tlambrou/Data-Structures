#!python

import sort
import unittest


class TestSort(unittest.TestCase):

    def test_bubble_sort(self):
        array = [7, 5, 1, 8, 3, 4, 4, 7, 3, 6, 2, 1, 8, 9, 0, 6]
        assert sort.bubble_sort(array) == [0, 1, 1, 2, 3, 3, 4, 4, 5, 6, 6, 7, 7, 8, 8, 9]

    def test_selection_sort(self):
        array = [7, 5, 1, 8, 3, 4, 4, 7, 3, 6, 2, 1, 8, 9, 0, 6]
        assert sort.selection_sort(array) == [0, 1, 1, 2, 3, 3, 4, 4, 5, 6, 6, 7, 7, 8, 8, 9]

    def test_insertion_sort(self):
        array = [7, 5, 1, 8, 3, 4, 4, 7, 3, 6, 2, 1, 8, 9, 0, 6]
        assert sort.insertion_sort(array) == [0, 1, 1, 2, 3, 3, 4, 4, 5, 6, 6, 7, 7, 8, 8, 9]

    def test_tree_sort(self):
        array = [7, 5, 1, 8, 3, 4, 4, 7, 3, 6, 2, 1, 8, 9, 0, 6]
        assert sort.tree_sort(array) == [0, 1, 1, 2, 3, 3, 4, 4, 5, 6, 6, 7, 7, 8, 8, 9]

    def test_counting_sort(self):
        array = [7, 5, 1, 8, 3, 4, 4, 7, 3, 6, 2, 1, 8, 9, 0, 6]
        assert sort.counting_sort(array) == [0, 1, 1, 2, 3, 3, 4, 4, 5, 6, 6, 7, 7, 8, 8, 9]

    def test_merge(self):
        list1 = [7, 5, 1, 8, 3, 4, 4, 7]
        list2 = [3, 6, 2, 1, 8, 9, 0, 6]
        list1 = sort.tree_sort(list1)
        list2 = sort.tree_sort(list2)
        assert sort.merge(list1=list1, list2=list2) == [0, 1, 1, 2, 3, 3, 4, 4, 5, 6, 6, 7, 7, 8, 8, 9]

    def test_merge_sort_nonrecursive(self):
        array = [7, 5, 1, 8, 3, 4, 4, 7, 3, 6, 2, 1, 8, 9, 0, 6]
        assert sort.merge_sort_nonrecursive(array) == [0, 1, 1, 2, 3, 3, 4, 4, 5, 6, 6, 7, 7, 8, 8, 9]

    def test_merge_sort_recursive(self):
        array = [7, 5, 1, 8, 3, 4, 4, 7, 3, 6, 2, 1, 8, 9, 0, 6]
        assert sort.merge_sort_recursive(array) == [0, 1, 1, 2, 3, 3, 4, 4, 5, 6, 6, 7, 7, 8, 8, 9]


if __name__ == '__main__':
    unittest.main()
