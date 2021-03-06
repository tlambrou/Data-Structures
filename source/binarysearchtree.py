#!python

from queue import LinkedQueue, ArrayQueue

class BinaryNode(object):

    def __init__(self, data=None):  # O(1)
        """Initialize this node with the given data"""
        self.data = data  # O(1)
        self.left = None  # O(1)
        self.right = None  # O(1)


    def __repr__(self):  # O(1)
        """Return a string representation of this node"""
        return 'Node({})'.format(repr(self.data))  # O(1)

    def is_leaf(self):  # O(1)
        """Check if the node is a leaf (has no children)"""
        if self.left is not None:  # O(1)
            return False  # O(1)
        if self.right is not None:  # O(1)
            return False  # O(1)
        return True  # O(1)

    def is_internal(self):
        """Check if the node is internal (has at least one child)"""
        return (not self.is_leaf())

    def height(self):
        """Return the number of edges on the longest downward path from this
        node to a descendant leaf node"""
        # TODO: Check if left child has a value and if so calculate its height
        # left_height = ... if self.left is not None else -1

        # TODO: Check if right child has a value and if so calculate its height
        # right_height = ... if self.right is not None else -1
        # Return one more than the greater of the left height and right height
        # return 1 + max(left_height, right_height)
        pass

    def is_single_baby_daddy(self):
        """Returns True if node has one child and returns False otherwise"""
        count = 0
        if self.left is not None:
            count += 1
        if self.right is not None:
            count += 1
        if count == 1:
            return True
        else:
            return False

    def is_double_baby_daddy(self):
        """Returns True if node has two children and returns False otherwise"""
        if self.left is None:
            return False
        if self.right is None:
            return False
        return True

class BinarySearchTree(object):

    def __init__(self, iterable=None):
        """Initialize this binary search tree; append the given items, if any"""
        self.root = None
        self.size = 0
        if iterable is not None:
            for item in iterable:
                self.insert(item)

    def is_empty(self):
        """"Return True if binary search tree is empty, False if not."""
        if self.root is None:
            return True
        else:
            return False

    def insert(self, data):
        """Insert a new node with data in order in the tree"""
        if self.is_empty():
            self.root = BinaryNode(data)
            self.size += 1
            return
        current = self.root
        inserted = False
        while inserted is False:
            if data >= current.data:
                if current.right is None:
                    current.right = BinaryNode(data)
                    inserted = True
                    self.size += 1
                else:
                    current = current.right
            elif data < current.data:
                if current.left is None:
                    current.left = BinaryNode(data)
                    inserted = True
                    self.size += 1
                else:
                    current = current.left

    def search(self, data):
        """Check if a node with data is present in the tree"""
        if self.is_empty():
            return None
        current = self.root
        while current.is_leaf() is False:
            if current.data == data:
                return current.data
            else:
                if data > current.data:
                    current = current.right
                elif data < current.data:
                    current = current.left
        if current.data == data:
            return current.data
        else:
            return None

    def delete(self, data):
        """Remove the node with data from the tree"""
        # If the tree is empty exit
        if self.is_empty():
            return
        # Set the current at the root
        current = self.root
        # Find the target node using find_node() method
        target = self.find_node(data)
        # 1st case: target node has no children (is a leaf)
        if target.is_leaf():
            # If the target is also the root...
            if target is self.root:
                # Remove the root and return
                self.root = None
                self.size -= 1
                return
            # Otherwise...
            else:
                # Find the parent node
                parent = self.find_parent_node(target)
                # Find which edge is the target
                if parent.right is target:
                    # Delete the node on the right and return
                    parent.right = None
                    self.size -= 1
                    return
                elif parent.left is target:
                    # Delete the node on the left and return
                    parent.left = None
                    self.size -= 1
                    return
                else:
                    raise ValueError('Something went wrong when finding the target and its parent')
        # 2nd case: target node has 1 child
        elif target.is_single_baby_daddy():
            # If the target is also the root...
            if target is self.root:
                # Find which child exists and make it the new root
                if target.right is None:
                    self.root = target.left
                    self.size -= 1
                    return
                elif target.left is None:
                    self.root = target.right
                    self.size -= 1
                    return
            else:
                # Otherwise find the parent node
                parent = self.find_parent_node(target)
                # If the target is to the right of the parent
                if parent.right is target:
                    # Find the target's child
                    if target.left is None:
                        # Point the parent to the target's child
                        parent.right = target.right
                        self.size -= 1
                        return
                    elif target.right is None:
                        # Point the parent to the target's child
                        parent.right = target.left
                        self.size -= 1
                        return
                # If the target is to the left of the parent
                elif parent.left is target:
                    # Find the target's child
                    if target.left is None:
                        # Point the parent to the target's child
                        parent.left = target.right
                        self.size -= 1
                        return
                    elif target.right is None:
                        # Point the parent to the target's child
                        parent.left = target.left
                        self.size -= 1
                        return
        # 3rd Case: target has 2 children
        elif target.is_double_baby_daddy():
            # If the target is the root
            if target is self.root:
                # Find in-order predecessor of target
                iop = self.find_rightiest_node(target.left)
                # Find in-order predecessor parent
                iop_parent = self.find_parent_node(iop)
                # If the IOP is the left branch of the target/root
                if iop is target.left:
                    # Set the right branch to point to the same node as the root
                    iop.right = target.right
                    # Promote IOP to the root
                    self.root = iop
                    self.size -= 1
                    return
                # Otherwise, if the IOP must be a right child of the target.left
                else:
                    # Point the IOP parent's right edge to the IOP's left node
                    iop_parent.right = iop.left
                    # Give the IOP the target's pointers
                    iop.left = target.left
                    iop.right = target.right
                    # Finally make the IOP the tree's root
                    self.root = iop
                    self.size -= 1
                    return
            # Otherwise (target is NOT the root)
            else:
                # Find the parent to the target
                parent = self.find_parent_node(target)
                # Find the IOP to the target
                iop = self.find_rightiest_node(target.left)
                # If the IOP is the target's left branch...
                if target.left is iop:
                    # Set the iop's right to the target's right branch
                    iop.right = target.right
                    # Determine which branch of the parent is pointing to the target
                    if parent.right is target:
                        # If right point it to the iop
                        parent.right = iop
                        self.size -= 1
                        return
                    elif parent.left is target:
                        # If left point it to the iop
                        parent.left = iop
                        self.size -= 1
                        return
                else:
                    # Find the IOP's parent
                    iop_parent = self.find_parent_node(iop)
                    # Point the IOP parent's right edge to the IOP's left node
                    iop_parent.right = iop.left
                    # Give the IOP the branch pointers of the target
                    iop.right = target.right
                    iop.left = target.left
                    # Determine which branch the target is to the parent and set it to the iop
                    if parent.right is target:
                        parent.right = iop
                        self.size -= 1
                        return
                    elif parent.left is target:
                        parent.left = iop
                        self.size -= 1
                        return


    def find_node(self, data):
        """Check if a node has the data and return the node"""
        if self.is_empty():
            return None
        current = self.root
        while current.is_leaf() is False:
            if current.data == data:
                return current
            else:
                if data > current.data:
                    current = current.right
                elif data < current.data:
                    current = current.left
        if current.data == data:
            return current
        else:
            return None

    def find_parent_node(self, target):
        if self.is_empty():
            return None
        current = self.root
        if current is target:
            raise ValueError('Data found in root node')
        while current.is_leaf() is False:
            if target.data > current.data:
                if current.right is target:
                    return current
                else:
                    current = current.right
            elif target.data < current.data:
                if current.left is target:
                    return current
                else:
                    current = current.left
        return None

    def find_rightiest_node(self, node):
        """Given a node, find descendant node most to the right of it"""
        current = node
        while current.right != None:
            current = current.right
        return current

    def items_in_order(self, node=None, items=None):
        """Return a list of all items in this binary search tree found using
        in-order traversal starting at the given node after the given items"""
        # Set up starting node and items list if not given
        if node is None:
            node = self.root
        if items is None:
            items = list()
        # TODO: Traverse left subtree, if it exists
        if node is not None:
            if node.left is not None:
                self.items_in_order(node.left, items)
        # TODO: Add this node's data to the items list
            items.append(node.data)
        # TODO: Traverse right subtree, if it exists
            if node.right is not None:
                self.items_in_order(node.right, items)
        # Return the items list to the original caller
        return items

    def items_pre_order(self, node=None, items=None):
        """Return a list of all items in this binary search tree found using
        pre-order traversal starting at the given node after the given items"""
        # Set up starting node and items list if not given
        if node is None:
            node = self.root
        if items is None:
            items = list()
        # TODO: Add this node's data to the items list
        if node is not None:
            items.append(node.data)
        # TODO: Traverse left subtree, if it exists
            if node.left is not None:
                self.items_pre_order(node.left, items)
        # TODO: Traverse right subtree, if it exists
            if node.right is not None:
                self.items_pre_order(node.right, items)
        # Return the items list to the original caller
        return items

    def items_post_order(self, node=None, items=None):
        """Return a list of all items in this binary search tree found using
        post-order traversal starting at the given node after the given items"""
        # Set up starting node and items list if not given
        if node is None:
            node = self.root
        if items is None:
            items = list()
        # TODO: Traverse left subtree, if it exists
        if node is not None:
            if node.left is not None:
                self.items_post_order(node.left, items)
        # TODO: Traverse right subtree, if it exists
            if node.right is not None:
                self.items_post_order(node.right, items)
        # TODO: Add this node's data to the items list
            items.append(node.data)
        # Return the items list to the original caller
        return items

    def items_level_order(self):
        """Return a list of all items in this binary search tree found using
        level-order traversal"""
        # TODO: Create a queue to store nodes not yet traversed in level-order
        queue = LinkedQueue()
        # Create an items list
        items = list()
        # TODO: Enqueue the root node if this tree is not empty
        if self.root is not None:
            queue.enqueue(self.root)
        # TODO: Loop until the queue is empty
        while queue.length() > 0:
            # TODO: Dequeue the node at the front of the queue
            node = queue.dequeue()
            # TODO: Add this node's data to the items list
            items.append(node.data)
            # TODO: Enqueue this node's left child if it exists
            if node.left is not None:
                queue.enqueue(node.left)
            # TODO: Enqueue this node's right child if it exists
            if node.right is not None:
                queue.enqueue(node.right)
        # Return the items list
        return items


def test_binary_search_tree():
    # Create a complete binary search tree of 3, 7, or 15 items in level-order
    # items = [2, 1, 3]
    items = [4, 2, 6, 1, 3, 5, 7]
    # items = [8, 4, 12, 2, 6, 10, 14, 1, 3, 5, 7, 9, 11, 13, 15]
    print('items: ' + str(items))

    bst = BinarySearchTree()
    print('tree: ' + str(bst))
    print('root: ' + str(bst.root))

    print('\nInserting items:')
    for item in items:
        bst.insert(item)
        # print('insert({})'.format(item))
        print('insert({}), size: {}'.format(item, bst.size))
        # print(bst)
    print('root: ' + str(bst.root))

    print('\nSearching for items:')
    for item in items:
        result = bst.search(item)
        print('search({}): {}'.format(item, result))
    item = 123
    result = bst.search(item)
    print('search({}): {}'.format(item, result))

    print('\nTraversing items:')
    print('items in-order:    ' + str(bst.items_in_order()))
    print('items pre-order:   ' + str(bst.items_pre_order()))
    print('items post-order:  ' + str(bst.items_post_order()))
    print('items level-order: ' + str(bst.items_level_order()))

class TreeMap(object):

    def __init__(self, iterable=None):
        self.tree = BinarySearchTree()
        self.root = self.tree.root
        self.size = self.tree.size
        if iterable is not None:
            for item in iterable:
                self.insert(item)

    def insert(self, data):
        if self.tree.is_empty():
            tup = (data, 1)
            self.tree.insert(tup)
            self.root = self.tree.root
            self.size = self.tree.size
            return
        elif self.root.data[0] == data:
            new_freq = self.root.data[1] + 1
            tup = (data, new_freq)
            self.root.data = tup
            return
        else:
            node = self.find_parent_node(data)
            current = self.tree.root
            if node is None:
                inserted = False
                tup = (data, 1)
                while inserted is False:
                    if data > current.data[0]:
                        if current.right is None:
                            current.right = BinaryNode(tup)
                            inserted = True
                            self.size += 1
                            self.tree.size += 1
                            return
                        else:
                            current = current.right
                    elif data <= current.data[0]:
                        if current.left is None:
                            current.left = BinaryNode(tup)
                            inserted = True
                            self.size += 1
                            self.tree.size += 1
                            return
                        else:
                            current = current.left
            elif node is not None:
                if node.data[0] < data:
                    node = node.right
                elif node.data[0] >= data:
                    node = node.left
                new_freq = (node.data[1]) + 1
                tup = (data, new_freq)
                node.data = tup
        return

    def find_parent_node(self, data):
        if self.tree.is_empty():
            return None
        current = self.root
        if current.data[0] == data:
            raise ValueError('Data found in root node')
        while current.is_leaf() is False:
            if data > current.data[0]:
                if current.right is not None:
                    if current.right.data[0] == data:
                        return current
                    else:
                        current = current.right
                else:
                    return None
            elif data < current.data[0]:
                if current.left is not None:
                    if current.left.data[0] == data:
                        return current
                    else:
                        current = current.left
                else:
                    return None
        return None

    def items_in_order(self, node=None, items=None):
        """Return a list of all items in this binary search tree found using
        in-order traversal starting at the given node after the given items"""
        # Set up starting node and items list if not given
        if node is None:
            node = self.tree.root
        if items is None:
            items = list()
        # TODO: Traverse left subtree, if it exists
        if node is not None:
            if node.left is not None:
                self.items_in_order(node.left, items)
        # TODO: Add this node's data to the items list
            freq = node.data[1]
            for i in range(0, freq):
                items.append(node.data[0])
        # TODO: Traverse right subtree, if it exists
            if node.right is not None:
                self.items_in_order(node.right, items)
        # Return the items list to the original caller
        return items


    def get_in_order_list(self):
        print("Get in-order List")
        return self.items_in_order()


    def search(self, data):
        if self.tree.is_empty():
            return None
        current = self.root
        while current.is_leaf() is False:
            if current.data[0] == data:
                return current
            else:
                if data > current.data[0] and current.right is not None:
                    current = current.right
                    print("Current was less than the data", current.data, current.right)
                elif data < current.data[0] and current.left is not None:
                    current = current.left
                    print("Current was greater than the data", current.data, current.left)

        if current.data[0] == data:
            return current
        else:
            return None

def test_tree_map():
    array = [7, 5, 1, 8, 3, 4, 4, 7, 3, 6, 2, 1, 8, 9, 0, 6]
    treemap = TreeMap(array)
    assert treemap.get_in_order_list() == [0, 1, 1, 2, 3, 3, 4, 4, 5, 6, 6, 7, 7, 8, 8, 9]

if __name__ == '__main__':
    test_binary_search_tree()
    print("---BEGIN TREEMAP---")
    test_tree_map()
