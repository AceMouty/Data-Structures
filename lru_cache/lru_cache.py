
"""
Terminology

Cache Hit: When the data you want is in the cache
Cache Miss: When you gave to go to primary storage to get the data

LRU Cache (Least Recently Used)
Cache has a limited size
LRU Cache discards the least recently used item in teh cache, when the cache is full

Sructs needed:

Hash Table: Need to be able to look something up with a key. Hash table will allow us to quickly look up cache
            entries by key
Doubly Linked List: Need to organize our data in least and most recently used data.
    - The DLL makes it easy to move data to the head O(1)
    - The DLL makes it easy to remove data from the tail O(1)

Most recently used: Most recently read or most recently added to the cache.
Least Recnely used: This will be discarded, the tail holds the least recently used item

Adding entries to the cache:
    - if the data exists
        - Check the hash with the provided key to see if the key is a key in the hash
        - Move the new entry to the head of the list
    - if not
        - If the hash is full, then we need to remove the tail (return del node)
        - Delete the tail pointer from hash table (ref del node for this)
        - create a new node in the list (return new node addr)
        - create a KVP in the hash that points to the new node (use created node addr)
    - finally
        - create a new node in the DLL (return new node addr)
        - Add Hash table entry that holds a pointer to the new DLL node (use created node addr)
    - return the found / new item

Get Item from the cache:
    - Ref steps above ^^^^
    - Return the node from setter fn (steps above)

Remove Item from the cache:
    - If the cache is overfull, delete the tail, return the removed node
    - Remove the tail pointer from the hash table wher KVP value == removed node value
"""
from doubly_linked_list import DoublyLinkedList


class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """

    def __init__(self, limit=10):
        self.cache = {}
        self.dll = DoublyLinkedList()
        self.limit = limit
        self.size = 0

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """

    def get(self, key):
        if key in self.cache.keys():
            self.dll.move_to_front(self.cache[key])
            return self.cache[key].value[1]
        else:
            return None

    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """

    def set(self, key, value):
        # if they key passed exists then update the value
        # and make it the head of the list
        if key in self.cache.keys():
            self.cache[key].value = (key, value)
            self.dll.move_to_front(self.cache[key])
            return self.cache[key]

        elif key not in self.cache.keys():

            self.size += 1
            self.cache[key] = self.dll.add_to_head((key, value))

            # remove the LRU obj if we are at capactiy
            if self.size > self.limit:
                self.size -= 1
                old_node = self.dll.remove_from_tail()
                del self.cache[old_node.value[0]]

            return self.cache[key]
