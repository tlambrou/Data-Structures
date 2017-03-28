#!python

from find import find
from find import find_index
import unittest

class TestFind(unittest.TestCase):

    def test_pattern_exists_inside_of_string(self):
        assert find('Rubber baby buggy bumpers', 'umpers') is True
        assert find('Tassos', 'ass') is True
        assert find('William W Wold', 'old') is True
        assert find('Fanisa Mlangeni', 'Fani') is True
        assert find('awesome', 'so') is True

    def test_pattern_does_not_exist_inside_of_string(self):
        assert find('Corey', 'cool') is False
        assert find('Madhur', 'awesome') is False
        assert find('Corey and Carlos', 'Corelos') is False
        assert find('Alan', 'enhance') is False

    def test_index_of_existent_pattern_in_string(self):
        assert find_index('Rubber baby buggy bumpers', 'umpers') is 19
        assert find_index('Tassos', 'ass') is 1
        assert find_index('William W Wold', 'old') is 11
        assert find_index('Fanisa Mlangeni', 'Fani') is 0
        assert find_index('awesome', 'so') is 3

    def test_index_of_inexistent_pattern_in_string(self):
        assert find_index('Corey', 'cool') is None
        assert find_index('Luca', 'awesome') is None
        assert find_index('Corey and Carlos', 'Corelos') is None
        assert find_index('Alan', 'enhance') is None

if __name__ == '__main__':
    unittest.main()
