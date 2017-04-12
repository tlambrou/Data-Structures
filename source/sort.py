#!python

from binarysearchtree import BinarySearchTree

def bubble_sort(array):
    in_order = False
    while in_order is False:
        in_order = True
        for i in range(0, len(array) - 1):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                in_order = False
    return array

def selection_sort(array):
    for i in range(0, len(array) - 1):
        running_smallest = i
        for k in range(i, len(array)):
            if array[k] < array[running_smallest]:
                running_smallest = k
        array[i], array[running_smallest] = array[running_smallest], array[i]
    return array

def insertion_sort(array):
    for i in range(1, len(array)):
        index = i
        while array[index] < array[index - 1] and index != 0:
            array[index], array[index - 1] = array[index - 1], array[index]
            index -= 1
    return array

def tree_sort(array):
    tree = BinarySearchTree(array)
    print(tree)
    return tree.items_in_order()
