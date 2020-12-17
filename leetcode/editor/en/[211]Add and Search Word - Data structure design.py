#Design a data structure that supports the following two operations: 
#
# 
#void addWord(word)
#bool search(word)
# 
#
# search(word) can search a literal word or a regular expression string containing only letters a-z or .. A . means it can represent any one letter. 
#
# Example: 
#
# 
#addWord("bad")
#addWord("dad")
#addWord("mad")
#search("pad") -> false
#search("bad") -> true
#search(".ad") -> true
#search("b..") -> true
# 
#
# Note: 
#You may assume that all words are consist of lowercase letters a-z. 
# Related Topics Backtracking Design Trie



#leetcode submit region begin(Prohibit modification and deletion)
class WordDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: None
        """
        p = self.root
        for ch in word:
            p = p.setdefault(ch, {})
        p['#'] = None

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        return self.helper(self.root, word, 0)

    def helper(self, p, word, i):
        if i>=len(word):
            return True if '#' in p else False
        if word[i]!='.':
            if word[i] in p: return self.helper(p[word[i]], word, i+1)
            else: return False
        else:
            ans = False
            for ch in p:
                if ch=='#': continue
                ans = ans or self.helper(p[ch], word, i+1)
            return ans
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
#leetcode submit region end(Prohibit modification and deletion)
