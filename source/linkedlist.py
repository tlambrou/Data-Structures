#!python

class Node(object):

    def __init__(self, data):
        """Initialize this node with the given data"""
        self.data = data
        self.next = None

    def __repr__(self):
        """Return a string representation of this node"""
        return 'Node({})'.format(repr(self.data))


class LinkedList(object):

    def __init__(self, iterable=None):
        """Initialize this linked list; append the given items, if any"""
        self.head = None
        self.tail = None
        self.size = 0
        if iterable:
            for item in iterable:
                self.append(item)

    def __str__(self):
        """Return a formatted string representation of this linked list"""
        items = ['({})'.format(repr(item)) for item in self.items()]
        return '[{}]'.format(' -> '.join(items))

    def __repr__(self):
        """Return a string representation of this linked list"""
        return 'LinkedList({})'.format(repr(self.items()))

    def items(self):
        """Return a list of all items in this linked list.
        Best and worst case running time: Theta(n) for n items in the list
        because we always need to loop through all n nodes."""
        # Create an empty list of results
        result = []  # Constant time to create a new list
        # Start at the head node
        current = self.head  # Constant time to assign a variable reference
        # Loop until the current node is None, which is one node past the tail
        while current is not None:  # Always n iterations because no early exit
            # Append the current node's data to the results list
            result.append(current.data)  # Constant time to append to a list
            # Skip to the next node
            current = current.next  # Constant time to reassign a variable
        # Now result contains the data from all nodes
        return result  # Constant time to return a list

    def is_empty(self):
        """Return True if this linked list is empty, or False"""
        return self.head is None

    def length(self):
        """Return the length of this linked list by traversing its nodes"""
        # Node counter initialized to zero
        node_count = 0
        # Start at the head node
        current = self.head
        # Loop until the current node is None, which is one node past the tail
        while current is not None:
            # Count one for this node
            node_count += 1
            # Skip to the next node
            current = current.next
        # Now node_count contains the number of nodes
        return node_count

    def get_at_index(self, index):
        """Return the item at the given index in this linked list, or
        raise ValueError if the given index is out of range of the list size"""
        # Check if the given index is out of range and if so raise an error
        if not (0 <= index < self.size):
            raise ValueError('List index out of range: {}'.format(index))
        # TODO: Find the node at the given index and return the node's data
        # Create a node count to check against the index
        node_count = 0
        # Start at the head node
        current = self.head
        # Loop until the current node is None, which is one node past the tail
        while current is not None:
            # Check to see if the current node count is the same as the index
            if node_count == index:
                # If they are equal return the data at the current node
                return current.data
            # If the index and the node count do not match
            else:
                # Skip to the next node
                current = current.next
                # Increment the node count
                node_count += 1

    def insert_at_index(self, index, item):
        """Insert the given item at the given index in this linked list, or
        raise ValueError if the given index is out of range of the list size"""
        # Check if the given index is out of range and if so raise an error
        if not (0 <= index <= self.size):
            raise ValueError('List index out of range: {}'.format(index))
        # TODO: Find the node before the given index and insert the item after
        # In the case that the given index is zero
        if index == 0:
            # Prepend the item to the beginning of the linked list
            self.prepend(item)
            return
        # Create a node count to check against the index
        next_node_index = 1
        # Start at the head node
        current = self.head
        # Loop until the current node is None, which is one node past the tail
        while current is not None:
            print("In the while loop ")
            # Check to see if the current node count is the same as the index
            if next_node_index == index:
                # Check if the index is the last element in the linked list
                if current.next is None:
                    # Append the item to the end
                    self.append(item)
                    return
                # Create a new node
                new_node = Node(item)
                # Point the new node's next to the current's next
                new_node.next = current.next
                # Poin the current's next to the new node
                current.next = new_node
                # Increment the size
                self.size += 1
                return
            # If the index and the node count do not match
            else:
                # Skip to the next node
                current = current.next
                # Increment the node count
                next_node_index += 1

    def append(self, item):  # O(1)
        """Insert the given item at the tail of this linked list"""
        # Create a new node to hold the given item
        new_node = Node(item)  # O(1)
        # Check if this linked list is empty
        if self.is_empty():  # O(1)
            # Assign head to new node
            self.head = new_node  # O(1)
        else:  # O(1)
            # Otherwise insert new node after tail
            self.tail.next = new_node  # O(1)
        # Update tail to new node regardless
        self.tail = new_node  # O(1)
        # Update the size
        self.size += 1  # O(1)

    def prepend(self, item):
        """Insert the given item at the head of this linked list"""
        # Create a new node to hold the given item
        new_node = Node(item)
        # Check if this linked list is empty
        if self.is_empty():
            # Assign tail to new node
            self.tail = new_node
        else:
            # Otherwise insert new node before head
            new_node.next = self.head
        # Update head to new node regardless
        self.head = new_node
        # Update the size
        self.size += 1

    def delete(self, item):  # O(n)
        """Delete the given item from this linked list, or raise ValueError"""
        # Start at the head node
        current = self.head  # O(1)
        # Keep track of the node before the one containing the given tiem
        previous = None  # O(1)
        # Create a flag to track if we have found the given item
        found = False  # O(1)
        # Loop until we have found the given item or the current node is None
        while not found and current is not None:  # O(n)
            # Check if the current node's data matches the given item
            if current.data == item:  # O(1)
                # We found data matching the given item, so update found flag
                found = True  # O(1)
            else:  # O(1)
                # Skip to the next node
                previous = current  # O(1)
                current = current.next  # O(1)
        # Check if we found the given item or we never did and reached the tail
        if found:  # O(1)
            # Check if we found a node in the middle of this linked list
            if current is not self.head and current is not self.tail:  # O(1)
                # Update the previous node to skip around the found node
                previous.next = current.next  # O(1)
                # Unlink the found node from its next node
                current.next = None  # O(1)
            # Check if we found a node at the head
            if current is self.head:  # O(1)
                # Update head to the next node
                self.head = current.next  # O(1)
                # Unlink the found node from the next node
                current.next = None  # O(1)
            # Check if we found a node at the tail
            if current is self.tail:  # O(1)
                # Check if there is a node before the found node
                if previous is not None:  # O(1)
                    # Unlink the previous node from the found node
                    previous.next = None  # O(1)
                # Update tail to the previous node regardless
                self.tail = previous  # O(1)
            # Update the size
            self.size -= 1  # O(1)
        else:  # O(1)
            # Otherwise raise an error to tell the user that delete has failed
            raise ValueError('Item not found: {}'.format(item))  # O(1)

    def find(self, quality):  # O(n)
        """Return an item from this linked list satisfying the given quality.
        Best case running time: Omega(1) if item is near the head of the list.
        Worst case running time: O(n) if item is near the tail of the list or
        not present and we need to loop through all n nodes in the list."""
        # Start at the head node
        current = self.head  # Constant time to assign a variable reference  # O(1)
        # Loop until the current node is None, which is one node past the tail
        while current is not None:  # Up to n iterations if we don't exit early  # O(n)
            # Check if the current node's data satisfyies the quality function
            if quality(current.data):  # Constant time to call quality function  # O(1)
                # We found data satisfying the quality function, so exit early
                return current.data  # Constant time to return data  # O(1)
            # Skip to the next node
            current = current.next  # Constant time to reassign a variable  # O(1)
        # We never found data satisfying quality, but have to return something
        return None  # Constant time to return None  # O(1)


def test_linked_list():
    ll = LinkedList()
    print(ll)

    print('Appending items:')
    ll.append('A')
    print(ll)
    ll.append('B')
    print(ll)
    ll.append('C')
    print(ll)
    print('head: ' + str(ll.head))
    print('tail: ' + str(ll.tail))
    print('size: ' + str(ll.size))
    print('length: ' + str(ll.length()))

    print('Getting items by index:')
    for index in range(ll.size):
        item = ll.get_at_index(index)
        print('get_at_index({}): {}'.format(index, repr(item)))

    print('Deleting items:')
    ll.delete('B')
    print(ll)
    ll.delete('C')
    print(ll)
    ll.delete('A')
    print(ll)
    print('head: ' + str(ll.head))
    print('tail: ' + str(ll.tail))
    print('size: ' + str(ll.size))
    print('length: ' + str(ll.length()))


if __name__ == '__main__':
    test_linked_list()
