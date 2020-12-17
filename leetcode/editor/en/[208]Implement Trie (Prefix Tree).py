#Implement a trie with insert, search, and startsWith methods. 
#
# Example: 
#
# 
#Trie trie = new Trie();
#
#trie.insert("apple");
#trie.search("apple");   // returns true
#trie.search("app");     // returns false
#trie.startsWith("app"); // returns true
#trie.insert("app");   
#trie.search("app");     // returns true
# 
#
# Note: 
#
# 
# You may assume that all inputs are consist of lowercase letters a-z. 
# All inputs are guaranteed to be non-empty strings. 
# 
# Related Topics Design Trie



#leetcode submit region begin(Prohibit modification and deletion)
class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}
        

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """
        p = self.root
        for ch in word:
            p = p.setdefault(ch, {})
        p['#'] = None
        

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        p = self.root
        for ch in word:
            if ch not in p: return False
            p = p[ch]
        if '#' in p: return True
        return False

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        p = self.root
        for ch in prefix:
            if ch not in p: return False
            p = p[ch]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
#leetcode submit region end(Prohibit modification and deletion)
