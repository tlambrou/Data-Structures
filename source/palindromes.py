#!python

# Hint: use string.ascii_letters (all letters in ASCII character set)
import string


def is_palindrome(text):
    """A string of characters is a palindrome if it reads the same forwards and
    backwards, ignoring punctuation, whitespace, and letter casing"""
    # implement is_palindrome_iterative and is_palindrome_recursive below, then
    # change this to call your implementation to verify it passes all tests
    assert isinstance(text, str)
    return is_palindrome_recursive(text)
    # return is_palindrome_recursive(text)


def is_palindrome_iterative(text):
    # TODO: implement the is_palindrome function iteratively here
    text = text.replace(" ", "").translate(None, string.punctuation)
    symetrical_chars = 0
    for i in range(0, len(text) - 1):
        if text[i].lower() == text[-i - 1].lower():
            symetrical_chars += 1
        else:
            return False
    print("Symetrical chars", symetrical_chars)
    return True

    # once implemented, change is_palindrome to call is_palindrome_iterative
    # to verify that your iterative implementation passes all tests


def is_palindrome_recursive(text, left=None, right=None):
    # TODO: implement the is_palindrome function recursively here
    text = text.replace(" ", "").translate(None, string.punctuation)
    if text == '':
        return True
    if left == None:
        left = 0
    if right == None:
        right = len(text) - 1
    if text[left].lower() == text[right].lower():
        if right == 0:
            return True
        else:
            return is_palindrome_recursive(text, left + 1, right - 1)
    else:
        return False

    # once implemented, change is_palindrome to call is_palindrome_recursive
    # to verify that your recursive implementation passes all tests


def main():
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) > 0:
        for arg in args:
            is_pal = is_palindrome(arg)
            result = 'PASS' if is_pal else 'FAIL'
            str_not = 'a' if is_pal else 'not a'
            print('{}: {} is {} palindrome'.format(result, repr(arg), str_not))
    else:
        print('Usage: {} string1 string2 ... stringN'.format(sys.argv[0]))
        print('  checks if each argument given is a palindrome')


if __name__ == '__main__':
    main()
