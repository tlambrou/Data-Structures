#!python

from binarysearchtree import BinarySearchTree

def bubble_sort(array):  # O(n^2-n)
    in_order = False  # O(1)
    while in_order is False:  # O(n)
        in_order = True  # O(1)
        for i in range(0, len(array) - 1):  # O(n)
            if array[i] > array[i + 1]:  # O(1)
                array[i], array[i + 1] = array[i + 1], array[i]  # O(1)
                in_order = False  # O(1)
    return array  # O(1)

def selection_sort(array):  # O(n^2)
    for i in range(0, len(array) - 1):  # O(n)
        running_smallest = i  # O(1)
        for k in range(i, len(array)):  # O(n/2)
            if array[k] < array[running_smallest]:  # O(1)
                running_smallest = k  # O(1)
        array[i], array[running_smallest] = array[running_smallest], array[i]  # O(1)
    return array  # O(1)

def insertion_sort(array):  # O(n*log(n))
    for i in range(1, len(array)):  # O(n)
        index = i  # O(1)
        while array[index] < array[index - 1] and index != 0:  # O(log(n))
            array[index], array[index - 1] = array[index - 1], array[index]  # O(1)
            index -= 1  # O(1)
    return array  # O(1)

def tree_sort(array):
    tree = BinarySearchTree(array)  # O(1)
    print(tree)
    return tree.items_in_order()
