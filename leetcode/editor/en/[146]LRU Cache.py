#Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and put. 
#
# get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1. 
#put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item. 
#
# The cache is initialized with a positive capacity. 
#
# Follow up: 
#Could you do both operations in O(1) time complexity? 
#
# Example: 
#
# 
#LRUCache cache = new LRUCache( 2 /* capacity */ );
#
#cache.put(1, 1);
#cache.put(2, 2);
#cache.get(1);       // returns 1
#cache.put(3, 3);    // evicts key 2
#cache.get(2);       // returns -1 (not found)
#cache.put(4, 4);    // evicts key 1
#cache.get(1);       // returns -1 (not found)
#cache.get(3);       // returns 3
#cache.get(4);       // returns 4
# 
#
# 
# Related Topics Design


import collections
#leetcode submit region begin(Prohibit modification and deletion)

class LRUCache2(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.dlist = collections.OrderedDict()

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.dlist: return -1
        val = self.dlist.pop(key)
        self.dlist[key] = val
        return val

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.dlist:  self.dlist.pop(key)
        self.dlist[key] = value
        if len(self.dlist) > self.capacity: self.dlist.popitem(last=False)


class LRUCache(object):
    class Node():
        def __init__(self, key, value, prev=None, next=None):
            self.key = key
            self.value = value
            self.prev = prev
            self.next = next

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.head = self.Node(None, None)
        self.tail = self.Node(None, None)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.map = {}

    def add_last(self, p):
        last = self.tail.prev
        last.next = p
        p.prev = last
        self.tail.prev = p
        p.next = self.tail

    def remove_first(self):
        first = self.head.next
        self.head.next = first.next
        first.next.prev = self.head
        return first

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.map:
            p = self.map[key]
            p.prev.next = p.next
            p.next.prev = p.prev
            self.add_last(p)
            return p.value
        else:
            return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key not in self.map:
            if len(self.map) == self.capacity:
                first = self.remove_first()
                del self.map[first.key]

            p = self.Node(key, value)
            self.map[key] = p
            self.add_last(p)
        else:
            p = self.map[key]
            p.value = value
            p.prev.next = p.next
            p.next.prev = p.prev
            self.add_last(p)
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
#leetcode submit region end(Prohibit modification and deletion)
