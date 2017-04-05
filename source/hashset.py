#!python

from linkedlist import LinkedList
from hashtable import HashTable


class HashSet(object):

    def __init__(self, elements=None):
        self.set = HashTable()
        for element in elements:
            self.set.set(key=element, value=None)

    def size(self):
        return self.set.size

    def contains(self, element):
        return self.set.contains(element)

    def add(self, element):
        self.set.set(key=element, value=None)

    def remove(self, element):
        self.set.delete(element)

    def union(self, other_set):
        union = HashTable()
        set_one = self.set.keys()
        set_two = other_set.set.keys()
        for element in set_one:
            union.set(key=element, value=None)
        for element in set_two:
            union.set(key=element, value=None)
        return union.keys()

    def intersection(self, other_set):
        intersect = HashTable()
        set_one = self.set.keys()
        for element in set_one:
            if other_set.set.contains(element) is True:
                intersect.set(key=element, value=None)
        return intersect.keys()

    def difference(self, other_set):
        difference = HashTable()
        set_one = self.set.keys()
        for element in set_one:
            if other_set.set.contains(element) is False:
                difference.set(key=element, value=None)
        return difference.keys()

    def is_subset(self, other_set):
        set_two = other_set.set.keys()
        count = 0
        for element in set_two:
            if self.contains(element):
                count += 1
            else:
                return False
        if count == len(set_two):
            return True



if __name__ == '__main__':
    test_hash_table()
