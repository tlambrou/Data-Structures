#!python

from linkedlist import LinkedList


class HashTable(object):

    def __init__(self, init_size=8):  # O(b)
        """Initialize this hash table with the given initial size"""
        self.buckets = [LinkedList() for i in range(init_size)]  # O(b)
        self.size = 0  # Count number of key-value entries     O(1)

    def __str__(self): #  O(n)
        """Return a formatted string representation of this hash table"""
        items = ['{}: {}'.format(repr(k), repr(v)) for k, v in self.items()] #  O(n)
        return '{' + ', '.join(items) + '}' #  O(1)

    def __repr__(self):  # O(1)
        """Return a string representation of this hash table"""
        return 'HashTable({})'.format(repr(self.items()))  # O(1)

    def _bucket_index(self, key):  # O(1)
        """Return the bucket index where the given key would be stored"""
        return hash(key) % len(self.buckets)  # O(1)

    def load_factor(self):   # O(1)
        """Return the load factor, the ratio of number of entries to buckets"""
        # TODO: Calculate load factor
        return float(self.length()) / float(len(self.buckets))  # O(1)

    def _resize(self, new_size=None):  # O(n^2)
        """Resize this hash table's buckets and rehash all key-value entries.
        Should be called automatically when load factor exceeds a threshold
        such as 0.75 after an insertion (when set is called with a new key)."""
        # If unspecified, choose new size dynamically based on current size
        if new_size is None:  # O(1)
            new_size = self.size * 2  # Double size    # O(1)
        # Option to reduce size if buckets are sparsely filled (low load factor)
        elif new_size is 0:  # O(1)
            new_size = self.size / 2  # Half size  # O(1)
        # TODO: Get a list to temporarily hold all current key-value entries
        tuples = self.items()  # O(n)
        # TODO: Create a new list of new_size total empty linked list buckets
        self.buckets = [LinkedList() for i in range(new_size)]    # O(b)
        self.size = 0   # O(1)
        # TODO: Insert each key-value entry into the new list of buckets,
        # which will rehash them into a new bucket index based on the new size
        for key, value in tuples:  # O(n) Total Loop Time: O(n^2)
            self.set(key, value)   # O(n)


    def keys(self):  # O(n)
        """Return a list of all keys in this hash table"""
        # Collect all keys in each of the buckets
        all_keys = []  # O(1)
        for bucket in self.buckets:  # O(b) Total loop time:   # O(n)
            for key, value in bucket.items():  # O(l)
                all_keys.append(key)  # O(1)
        return all_keys  # O(1)

    def values(self):  # O(n)
        """Return a list of all values in this hash table"""
        # Collect all values in each of the buckets
        all_values = []  # O(1)
        for bucket in self.buckets:  # O(b) Total loop time:   # O(n)
            for key, value in bucket.items():  # O(l)
                all_values.append(value)  # O(1)
        return all_values  # O(1)

    def items(self):  # O(n)
        """Return a list of all entries (key-value pairs) in this hash table"""
        # Collect all pairs of key-value entries in each of the buckets
        all_items = []  # O(1)
        for bucket in self.buckets:  # O(b) Total Loop Time: O(n)
            all_items.extend(bucket.items())   # O(l)
        return all_items  # O(1)

    def __iter__(self):
        for key in self.keys():
            yield key

    def length(self):   # O(n)
        """Return the number of key-value entries by traversing its buckets"""
        # Count number of key-value entries in each of the buckets
        item_count = 0  # O(1)
        for bucket in self.buckets:  # O(b) Total for loop:   # O(n)
            item_count += bucket.length()  # O(l)
        return item_count  # O(1)
        # Equivalent to this list comprehension:
        #return sum(bucket.length() for bucket in self.buckets)

    def contains(self, key):  # O(l)
        """Return True if this hash table contains the given key, or False"""
        # Find the bucket the given key belongs in
        index = self._bucket_index(key)  # O(1)
        bucket = self.buckets[index]  # O(1)
        # Check if an entry with the given key exists in that bucket
        entry = bucket.find(lambda (k, v): k == key)  # O(l)
        return entry is not None  # True or False  # O(1)

    def get(self, key):  # O(l)
        """Return the value associated with the given key, or raise KeyError"""
        # Find the bucket the given key belongs in
        index = self._bucket_index(key)  # O(1)
        bucket = self.buckets[index]  # O(1)
        # Find the entry with the given key in that bucket, if one exists
        entry = bucket.find(lambda (k, v): k == key)  # O(l)
        if entry is not None:  # Found  # O(1)
            # Return the given key's associated value
            assert isinstance(entry, tuple)  # O(1)
            assert len(entry) == 2  # O(1)
            return entry[1]  # O(1)
        else:  # Not found  # O(1)
            raise KeyError('Key not found: {}'.format(key))  # O(1)

    def set(self, key, value):  # O(n)
        """Insert or update the given key with its associated value"""
        # Find the bucket the given key belongs in
        index = self._bucket_index(key)  # O(1)
        bucket = self.buckets[index]  # O(1)
        # Find the entry with the given key in that bucket, if one exists
        # Check if an entry with the given key exists in that bucket
        entry = bucket.find(lambda (k, v): k == key)  # O(b)
        if entry is not None:  # Found   # O(1)
            # In this case, the given key's value is being updated
            # Remove the old key-value entry from the bucket first
            bucket.delete(entry)  # O(l)
            self.size -= 1  # O(1)
        # Insert the new key-value entry into the bucket in either case
        bucket.append((key, value))  # O(l)
        self.size += 1  # O(1)
        # TODO: Check if the load factor exceeds a threshold such as 0.75
        if self.load_factor() > 0.75:   # O(1)
        # TODO: If so, automatically resize to reduce the load factor
            self._resize()   # O(n)

    def delete(self, key):  # O(l)
        """Delete the given key and its associated value, or raise KeyError"""
        # Find the bucket the given key belongs in
        index = self._bucket_index(key)   # O(1)
        bucket = self.buckets[index]  # O(1)
        # Find the entry with the given key in that bucket, if one exists
        entry = bucket.find(lambda (k, v): k == key)  # O(l)
        if entry is not None:  # Found   # O(1)
            # Remove the key-value entry from the bucket
            bucket.delete(entry)  # O(l)
            self.size -= 1  # O(1)
        else:  # Not found
            raise KeyError('Key not found: {}'.format(key))   # O(1)


def test_hash_table():
    ht = HashTable(4)
    print('HashTable: ' + str(ht))

    print('Setting entries:')
    ht.set('I', 1)
    print('set(I, 1): ' + str(ht))
    ht.set('V', 5)
    print('set(V, 5): ' + str(ht))
    print('size: ' + str(ht.size))
    print('length: ' + str(ht.length()))
    print('buckets: ' + str(len(ht.buckets)))
    print('load_factor: ' + str(ht.load_factor()))
    ht.set('X', 10)
    print('set(X, 10): ' + str(ht))
    ht.set('L', 50)  # Should trigger resize
    print('set(L, 50): ' + str(ht))
    print('size: ' + str(ht.size))
    print('length: ' + str(ht.length()))
    print('buckets: ' + str(len(ht.buckets)))
    print('load_factor: ' + str(ht.load_factor()))

    print('Getting entries:')
    print('get(I): ' + str(ht.get('I')))
    print('get(V): ' + str(ht.get('V')))
    print('get(X): ' + str(ht.get('X')))
    print('get(L): ' + str(ht.get('L')))
    print('contains(X): ' + str(ht.contains('X')))
    print('contains(Z): ' + str(ht.contains('Z')))

    print('Deleting entries:')
    ht.delete('I')
    print('delete(I): ' + str(ht))
    ht.delete('V')
    print('delete(V): ' + str(ht))
    ht.delete('X')
    print('delete(X): ' + str(ht))
    ht.delete('L')
    print('delete(L): ' + str(ht))
    print('contains(X): ' + str(ht.contains('X')))
    print('size: ' + str(ht.size))
    print('length: ' + str(ht.length()))
    print('buckets: ' + str(len(ht.buckets)))
    print('load_factor: ' + str(ht.load_factor()))


if __name__ == '__main__':
    test_hash_table()
