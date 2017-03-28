#!python

import string

def find(string, pattern):
    assert isinstance(string, str)
    assert isinstance(pattern, str)
    return find_recursive(string, pattern)
    # once implemented, will return True if string contains pattern and False if not
    # this is the iterative implementation

def find_iterative(string, pattern):
    for i in range(0, len(string) - len(pattern) + 1):
        j = len(pattern) + i
        if string[i:j] == pattern:
            return True
    return False

def find_recursive(string, pattern, index=None):
    if index == None:
        index = 0
    if index > len(string) - len(pattern) + 1:
        return False
    elif string[index:index + len(pattern)] == pattern:
        return True
    else:
        return find_recursive(string, pattern, index + 1)

def find_index(string, pattern):
    assert isinstance(string, str)
    assert isinstance(pattern, str)
    return find_index_recursive(string, pattern)
    # once implemented, will return True if string contains pattern and False if not
    # this is the iterative implementation

def find_index_iterative(string, pattern):
    for i in range(0, len(string) - len(pattern) + 1):
        j = len(pattern) + i
        if string[i:j] == pattern:
            return i
    return None

def find_index_recursive(string, pattern, index=None):
    if index == None:
        index = 0
    print('Index: ', index)
    if index > len(string) - len(pattern) + 2:
        return None
    elif string[index:index + len(pattern)] == pattern:
        return index
    else:
        return find_index_recursive(string, pattern, index + 1)

def main():
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) > 0:
        findstr = find(args[0], args[1])
        result = 'PASS' if findstr else 'FAIL'
        str_not = 'in' if findstr else 'not in'
        print('{}: {} is {} the pattern'.format(result, repr(args[1]), str_not))
        print("Results: ", find_index_recursive(args[0], args[1]))
    else:
        print('Usage: {} string1 string2 ... stringN'.format(sys.argv[0]))
        print('  checks if second argument is in the first argument')


if __name__ == '__main__':
    main()
