#!python

def linear_search(array, item):
    """return the first index of item in array or None if item is not found"""
    # implement linear_search_iterative and linear_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    return linear_search_iterative(array, item)
    # return linear_search_recursive(array, item)


def linear_search_iterative(array, item):
    # loop over all array values until item is found
    for index, value in enumerate(array):
        if item == value:
            return index  # found
    return None  # not found


def linear_search_recursive(array, item, index=0):
    # TODO: implement linear search recursively here
    if array[index] == item:
        return index
    else:
        return linear_search_recursive(array, item, index + 1)
    # once implemented, change linear_search to call linear_search_recursive
    # to verify that your recursive implementation passes all tests below


def binary_search(array, item):
    """return the index of item in sorted array or None if item is not found"""
    # implement binary_search_iterative and binary_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    return binary_search_recursive(array, item)
    # return binary_search_recursive(array, item)


def binary_search_iterative(array, item):
    # TODO: implement binary search iteratively here
    upper = len(array) - 1
    lower = 0
    index = int(((upper - lower) / 2) + lower)
    last_index = index
    count = 0
    while array[index] != item and count is not len(array) + 2:
        if lower == upper - 1:
            index = upper
            lower = upper
        # print("array[index] = ", array[index], "item = ", item, "index = ", index, "lower = ", lower, "upper = ", upper)
        # print("Boolean: ", array[index] > item)
        if array[index] > item:
            upper = index
        elif array[index] < item:
            lower = index
        index = int(((upper - lower) / 2) + lower)
        count += 1
    if count == len(array) + 1 and array[index] != item:
        return None
    elif array[index] == item:
        return index

    # once implemented, change binary_search to call binary_search_iterative
    # to verify that your iterative implementation passes all tests below


def binary_search_recursive(array, item, left=None, right=None):
    # TODO: implement binary search recursively here
    if left == None:
        left = 0
    if right == None:
        right = len(array) - 1
    index = int(((right - left) / 2) + left)
    # print("array[index] = ", array[index], "item = ", item, "index = ", index, "left = ", left, "right = ", right)
    # print("Boolean: ", array[index] > item)
    if array[index] == item:
        return index
    else:
        if array[index] > item:
            right = index
        elif array[index] < item:
            left = index
        if left == right - 1:
            if array[left] == item:
                return left
            elif array[right] == item:
                return right
            else:
                return None
        return binary_search_recursive(array, item, left, right)
    # once implemented, change binary_search to call binary_search_recursive
    # to verify that your recursive implementation passes all tests below
