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
        # Check to see if we have finished sorting the first list
        if index1 == len(list1):
            for i in range(index2, len(list2)):
                result.append(list2[i])
        # Check to see if we have finished sorting the second list
        elif index2 == len(list2):
            for i in range(index1, len(list1)):
                result.append(list1[i])
        else:
        # Append the smaller element of each list
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

def merge_sort_recursive(list1):
    # Check to see if the list is of length 1
    if len(list1) <= 1:  # Base case
        # Return the input as-is (it's already sorted!)
        return list1
    else:
        # 1. Divide: split input into two sublists of half size
        midpoint = len(list1) / 2
        temp1 = list1[:midpoint]
        temp2 = list1[midpoint:]
        # 2. Conquer: sort sublists recursively
        sorted1 = merge_sort_recursive(temp1)
        sorted2 = merge_sort_recursive(temp2)
        # 3. Combine: merge two sorted sublists
        # This is where the magic happens!
        merged = merge(sorted1, sorted2)
        return merged
