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

if __name__ == '__main__':
    unittest.main()
