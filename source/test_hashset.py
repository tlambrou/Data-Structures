#!python

from hashset import HashSet
import unittest


class HashSetTest(unittest.TestCase):

    def test_init(self):
        elements = [1, 2, 3, 4, 5]
        hs = HashSet(elements)
        assert hs.set.size == 5

    def test_size(self):
        hs = HashSet([5, 2, 6, 1, 3])
        assert hs.size() == 5
        hs.add(42)
        assert hs.size() == 6
        hs.add(21)
        assert hs.size() == 7
        hs.remove(42)
        assert hs.size() == 6

    def test_contains(self):
        elements = [2, 4, 6, 8]
        hs = HashSet(elements)
        assert hs.contains(2) is True
        assert hs.contains(4) is True
        assert hs.contains(8) is True
        assert hs.contains(20) is False

    def test_add_and_remove(self):
        elements = [1, 2, 3]
        hs = HashSet(elements)
        hs.add(4)
        hs.add(5)
        hs.add(6)
        hs.add(7)
        assert hs.contains(2) is True
        assert hs.contains(4) is True
        assert hs.contains(5) is True
        assert hs.contains(6) is True
        assert hs.contains(7) is True
        assert hs.contains(21) is False
        hs.remove(7)
        assert hs.contains(7) is False
        hs.remove(6)
        assert hs.contains(6) is False
        hs.remove(5)
        assert hs.contains(5) is False
        hs.remove(4)
        assert hs.contains(4) is False
        assert hs.size() == 3

    def test_union(self):
        set_one = [0, 1, 2, 3, 4, 5]
        set_two = [3, 4, 5, 6, 7, 8]
        hs_one = HashSet(set_one)
        hs_two = HashSet(set_two)
        assert hs_one.size() == 6
        assert hs_two.size() == 6
        assert hs_one.union(hs_two).size() == 9
        # assert hs_one.union(hs_two).set == HashSet([0, 1, 2, 3, 4, 5, 6, 7, 8]).set

    def test_intersection(self):
        set_one = [0, 1, 2, 3, 4, 5]
        set_two = [3, 4, 5, 6, 7, 8]
        hs_one = HashSet(set_one)
        hs_two = HashSet(set_two)
        assert hs_one.size() == 6
        assert hs_two.size() == 6
        assert hs_one.intersection(hs_two).size() == 3
        # assert hs_one.intersection(hs_two).set == HashSet([3, 4, 5]).set

    def test_difference(self):
        set_one = [0, 1, 2, 3, 4, 5]
        set_two = [3, 4, 5, 6, 7, 8]
        hs_one = HashSet(set_one)
        hs_two = HashSet(set_two)
        assert hs_one.size() == 6
        assert hs_two.size() == 6
        assert hs_one.difference(hs_two).size() == 6
        # assert hs_one.difference(hs_two).set == HashSet([0, 1, 2, 6, 7, 8]).set

    def test_is_subset(self):
        set_one = [0, 1, 2, 3, 4, 5]
        set_two = [3, 4, 5]
        hs_one = HashSet(set_one)
        hs_two = HashSet(set_two)
        assert hs_one.is_subset(hs_two) is False
        assert hs_two.is_subset(hs_one) is True


if __name__ == '__main__':
    unittest.main()
