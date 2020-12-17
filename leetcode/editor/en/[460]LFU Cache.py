 #Design and implement a data structure for Least Frequently Used (LFU) cache. It should support the following operations: get and put.
#
# get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1. 
#put(key, value) - Set or insert the value if the key is not already present. When the cache reaches its capacity, it should invalidate the least frequently used item before inserting a new item. For the purpose of this problem, when there is a tie (i.e., two or more keys that have the same frequency), the least recently used key would be evicted. 
#
# Note that the number of times an item is used is the number of calls to the get and put functions for that item since it was inserted. This number is set to zero when the item is removed. 
#
# 
#
# Follow up: 
#Could you do both operations in O(1) time complexity? 
#
# 
#
# Example: 
#
# 
#LFUCache cache = new LFUCache( 2 /* capacity */ );
#
#cache.put(1, 1);
#cache.put(2, 2);
#cache.get(1);       // returns 1
#cache.put(3, 3);    // evicts key 2
#cache.get(2);       // returns -1 (not found)
#cache.get(3);       // returns 3.
#cache.put(4, 4);    // evicts key 1.
#cache.get(1);       // returns -1 (not found)
#cache.get(3);       // returns 3
#cache.get(4);       // returns 4
# 
#
# 
# Related Topics Design


#leetcode submit region begin(Prohibit modification and deletion)


class LFUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.key2freq = {}
        self.freq2lru = {}
        self.min_freq = 0

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.key2freq: return -1
        freq = self.key2freq[key]
        val = self.freq2lru[freq][key]
        self.freq2lru[freq].pop(key)
        if not self.freq2lru[freq]:
            self.freq2lru.pop(freq)
            if self.min_freq == freq: self.min_freq += 1
        freq += 1
        self.key2freq[key] = freq
        if freq not in self.freq2lru: self.freq2lru[freq] = collections.OrderedDict()
        self.freq2lru[freq][key] = val
        return val

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if self.capacity == 0: return
        if key in self.key2freq:
            freq = self.key2freq[key]
            self.freq2lru[freq][key] = value
            self.get(key)
            return

        if len(self.key2freq) == self.capacity:
            k, v = self.freq2lru[self.min_freq].popitem(last=False)
            if not self.freq2lru[self.min_freq]: self.freq2lru.pop(self.min_freq)
            self.key2freq.pop(k)

        freq = 1
        self.key2freq[key] = freq
        if freq not in self.freq2lru: self.freq2lru[freq] = collections.OrderedDict()
        self.freq2lru[freq][key] = value
        self.min_freq = 1


        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
#leetcode submit region end(Prohibit modification and deletion)
