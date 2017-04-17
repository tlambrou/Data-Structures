#!python

from binarysearchtree import BinarySearchTree, TreeMap

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
    tree = BinarySearchTree(array)  # O(n*log(n))
    return tree.items_in_order()

def counting_sort(array):
    treemap = TreeMap(array)
    return treemap.get_in_order_list()

def merge(list1, list2):
    index1 = 0
    index2 = 0
    result = []
    while len(result) is not (len(list1) + len(list2)):
        if index1 == len(list1):
            for i in range(index2, len(list2)):
                result.append(list2[i])
        elif index2 == len(list2):
            for i in range(index1, len(list1)):
                result.append(list1[i])
        else:
            if list1[index1] <= list2[index2]:
                result.append(list1[index1])
                index1 += 1
            elif list1[index1] > list2[index2]:
                result.append(list2[index2])
                index2 += 1
    return result

def merge_sort_nonrecursive(items):
    midpoint = len(items) / 2
    list1 = items[:midpoint]
    list2 = items[midpoint:]
    list1 = tree_sort(list1)
    list2 = counting_sort(list2)
    return merge(list1, list2)

def merge_sort_recursive(list1, list2=None):
    if len(list1) == 1 and len(list2) == 1:
        print("Merge condition met", list1, list2)
        return merge(list1, list2)
    else:
        if len(list1) != 1:
            print("Len of list1 not 1 | Length: ", len(list1))
            midpoint = len(list1) / 2
            temp1 = list1[:midpoint]
            print("Temp1: ", temp1)
            temp2 = list1[midpoint:]
            print("Temp2: ", temp2)
            merged1 = merge_sort_recursive(temp1, temp2)
        merged2 = []
        if list2 is not None:
            if len(list2) != 1:
                print("Len of list2 not 1 | Length: ", len(list2))
                midpoint = len(list2) / 2
                temp1 = list2[:midpoint]
                print("Temp1: ", temp1)
                temp2 = list2[midpoint:]
                print("Temp2: ", temp2)
                merged2 = merge_sort_recursive(temp1, temp2)
        return merge(merged1, merged2)
