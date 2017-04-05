#!python

from linkedlist import LinkedList
from hashtable import HashTable


class HashSet(object):

    def __init__(self, elements=None):
        self.set = HashTable()
        if elements is not None:
            for element in elements:
                self.set.set(key=element, value=None)

    def __iter__(self):
        for key in self.set.keys():
            yield key

    def size(self):
        return self.set.size

    def contains(self, element):
        return self.set.contains(element)

    def add(self, element):
        self.set.set(key=element, value=None)

    def remove(self, element):
        self.set.delete(element)

    def union(self, other_set):
        union = HashSet()
        set_one = self.set.keys()
        set_two = other_set.set.keys()
        for element in set_one:
        # This works if HashTable implements a __iter__ method
        # for element in self.set:
            union.add(element)
        for element in set_two:
            union.add(element)
        return union

    def intersection(self, other_set):
        intersect = HashSet()
        set_one = self.set.keys()
        for element in set_one:
            if other_set.set.contains(element) is True:
                intersect.add(element)
        return intersect

    def difference(self, other_set):
        difference = HashSet()
        set_one = self.set.keys()
        set_two = other_set.set.keys()
        for element in set_one:
            if other_set.set.contains(element) is False:
                difference.add(element)
        for element in set_two:
            if self.set.contains(element) is False:
                difference.add(element)
        return difference

    def is_subset(self, other_set):
        set_one = self.set.keys()
        for element in set_one:
            if other_set.contains(element) is False:
                return False
        return True


if __name__ == '__main__':
    test_hash_table()
