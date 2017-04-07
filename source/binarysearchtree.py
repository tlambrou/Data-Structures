#!python

class BinaryNode(object):

    def __init__(self, data=None):
        """Initialize this node with the given data"""
        self.data = data
        self.left = None
        self.right = None


    def __repr__(self):
        """Return a string representation of this node"""
        return 'Node({})'.format(repr(self.data))

    def is_leaf(self):
        """Check if the node is a leaf (has no children)"""
        if self.left is not None:
            return False
        if self.right is not None:
            return False
        return True

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
            if data > current.data:
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


if __name__ == '__main__':
    test_binary_search_tree()
