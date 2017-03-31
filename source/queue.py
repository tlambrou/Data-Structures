#!python

from linkedlist import LinkedList


# implement LinkedQueue below, then change the assignment at the bottom
# to use this Queue implementation to verify it passes all tests
class LinkedQueue(object):

    def __init__(self, iterable=None):
        """Initialize this queue and enqueue the given items, if any"""
        # Initialize a new linked list to store the items
        self.list = LinkedList()
        if iterable:
            for item in iterable:
                self.enqueue(item)

    def __repr__(self):
        """Return a string representation of this queue"""
        return 'Queue({} items, top={})'.format(self.length(), self.front())

    def is_empty(self):
        """Return True if this queue is empty, or False otherwise"""
        # TODO: Check if empty
        if self.list.head is None:
            return True
        else:
            return False

    def length(self):
        """Return the number of items in this queue"""
        # TODO: Count number of items
        if self.is_empty() is True:
            return 0
        else:
            length = 1
            current = self.list.head
            while current.next != None:
                length += 1
                current = current.next
            return length

    def enqueue(self, item):
        """Insert the given item at the back of this queue"""
        # TODO: Insert given item
        self.list.append(item)

    def front(self):
        """Return the item at the front of this queue without removing it,
        or None if this queue is empty"""
        # TODO: Return front item, if any
        if self.is_empty() is True:
            return None
        else:
            return self.list.head.data

    def dequeue(self):
        """Remove and return the item at the front of this queue,
        or raise ValueError if this queue is empty"""
        # TODO: Remove and return front item, if any
        if self.is_empty() is False and self.length() > 1:
            return_value = self.list.head.data
            self.list.head = self.list.head.next
            self.list.size -= 1
            return return_value
        elif self.list.size == 1:
            return_value = self.list.tail.data
            self.list.tail = None
            self.list.head = None
            self.list.size -= 1
            return return_value
        else:
            raise ValueError('Queue is empty')


# implement ArrayQueue below, then change the assignment at the bottom
# to use this Queue implementation to verify it passes all tests
class ArrayQueue(object):

    def __init__(self, iterable=None):
        """Initialize this queue and enqueue the given items, if any"""
        # Initialize a new dynamic array to store the items
        self.list = list()
        if iterable:
            for item in iterable:
                self.enqueue(item)

    def __repr__(self):
        """Return a string representation of this queue"""
        return 'Queue({} items, top={})'.format(self.length(), self.front())

    def is_empty(self):
        """Return True if this queue is empty, or False otherwise"""
        # TODO: Check if empty
        if len(self.list) == 0:
            return True
        else:
            return False

    def length(self):
        """Return the number of items in this queue"""
        # TODO: Count number of items
        return len(self.list)

    def enqueue(self, item):
        """Insert the given item at the back of this queue"""
        # TODO: Insert given item
        self.list.append(item)

    def front(self):
        """Return the item at the front of this queue without removing it,
        or None if this queue is empty"""
        # TODO: Return front item, if any
        if self.is_empty() is True:
            return None
        else:
            return self.list[0]

    def dequeue(self):
        """Remove and return the item at the front of this queue,
        or raise ValueError if this queue is empty"""
        # TODO: Remove and return front item, if any
        if self.is_empty() is True:
            raise ValueError('Queue is empty')
        else:
            return_value = self.front()
            self.list.pop(0)
            return return_value

# implement LinkedQueue and ArrayQueue above, then change the assignment below
# to use each of your Queue implementations to verify they each pass all tests
# Queue = LinkedQueue
Queue = ArrayQueue
