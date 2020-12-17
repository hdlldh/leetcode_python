#Implement a data structure supporting the following operations: 
#
# 
# 
# Inc(Key) - Inserts a new key with value 1. Or increments an existing key by 1. Key is guaranteed to be a non-empty string. 
# Dec(Key) - If Key's value is 1, remove it from the data structure. Otherwise decrements an existing key by 1. If the key does not exist, this function does nothing. Key is guaranteed to be a non-empty string. 
# GetMaxKey() - Returns one of the keys with maximal value. If no element exists, return an empty string "". 
# GetMinKey() - Returns one of the keys with minimal value. If no element exists, return an empty string "". 
# 
# 
#
# 
#Challenge: Perform all these in O(1) time complexity.
# Related Topics Design



#leetcode submit region begin(Prohibit modification and deletion)
class Vnode(object):
    def __init__(self, key, val):
        self.keys = set()
        self.keys.add(key)
        self.value = val
        self.prev = None
        self.next = None

class AllOne(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = Vnode(-1, -1)
        self.tail = Vnode(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.key2pos = {}

    def inc(self, key):
        """
        Inserts a new key <Key> with value 1. Or increments an existing key by 1.
        :type key: str
        :rtype: None
        """
        if key not in self.key2pos:
            curPos = self.head
            curVal = 0
        else:
            curPos = self.key2pos[key]
            curVal = curPos.value
        if curPos.next.value != curVal + 1:
            t = Vnode(key, curVal + 1)
            curPos.next.prev = t
            t.next = curPos.next
            curPos.next = t
            t.prev = curPos
            self.key2pos[key] = t
        else:
            curPos.next.keys.add(key)
            self.key2pos[key] = curPos.next
        if key in curPos.keys: curPos.keys.remove(key)
        if curPos != self.head and not curPos.keys:
            curPos.prev.next = curPos.next
            curPos.next.prev = curPos.prev

    def dec(self, key):
        """
        Decrements an existing key by 1. If Key's value is 1, remove it from the data structure.
        :type key: str
        :rtype: None
        """
        if key not in self.key2pos: return
        curPos = self.key2pos[key]
        curVal = curPos.value
        if curVal > 1:
            if curPos.prev.value != curVal -1 :
                t = Vnode(key, curVal -1)
                curPos.prev.next = t
                t.prev = curPos.prev
                curPos.prev = t
                t.next = curPos
                self.key2pos[key] = t
            else:
                curPos.prev.keys.add(key)
                self.key2pos[key] = curPos.prev
        else: self.key2pos.pop(key)
        curPos.keys.remove(key)
        if not curPos.keys:
            curPos.prev.next = curPos.next
            curPos.next.prev = curPos.prev


    def getMaxKey(self):
        """
        Returns one of the keys with maximal value.
        :rtype: str
        """
        if self.head.next != self.tail:
            return list(self.tail.prev.keys)[0]
        else:
            return ""

    def getMinKey(self):
        """
        Returns one of the keys with Minimal value.
        :rtype: str
        """
        if self.head.next != self.tail:
            return list(self.head.next.keys)[0]
        else:
            return ""
        


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()
#leetcode submit region end(Prohibit modification and deletion)
