#
#Implement a MapSum class with insert, and sum methods.
# 
#
# 
#For the method insert, you'll be given a pair of (string, integer). The string represents the key and the integer represents the value. If the key already existed, then the original key-value pair will be overridden to the new one.
# 
#
# 
#For the method sum, you'll be given a string representing the prefix, and you need to return the sum of all the pairs' value whose key starts with the prefix.
# 
#
# Example 1: 
# 
#Input: insert("apple", 3), Output: Null
#Input: sum("ap"), Output: 3
#Input: insert("app", 2), Output: Null
#Input: sum("ap"), Output: 5
# 
# 
# Related Topics Trie



#leetcode submit region begin(Prohibit modification and deletion)
class MapSum(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.map = {}

    def insert(self, key, val):
        """
        :type key: str
        :type val: int
        :rtype: None
        """
        if key not in self.map: self.map[key] = [0, 0]
        diff = val - self.map[key][0]
        self.map[key][0] = val
        n = len(key)
        for i in range(n-1):
            if key[:i+1] not in self.map: self.map[key[:i+1]] = [0, 0]
            self.map[key[:i+1]][1] += diff

    def sum(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        if prefix not in self.map: return 0
        return sum(self.map[prefix])

class TrieNode(object):
    def __init__(self):
        self.children = {}
        self.score = 0
class MapSum(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()
        self.map = {}

    def insert(self, key, val):
        """
        :type key: str
        :type val: int
        :rtype: None
        """
        delta = val - self.map.get(key, 0)
        self.map[key] = val
        p = self.root
        for ch in key:
            p = p.children.setdefault(ch, TrieNode())
            p.score += delta

    def sum(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        p = self.root
        for ch in prefix:
            if ch not in p.children:return 0
            p = p.children[ch]
        return p.score


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)
#leetcode submit region end(Prohibit modification and deletion)
