# Implement the StreamChecker class as follows: 
# 
#  
#  StreamChecker(words): Constructor, init the data structure with the given wor
# ds. 
#  query(letter): returns true if and only if for some k >= 1, the last k charac
# ters queried (in order from oldest to newest, including this letter just queried
# ) spell one of the words in the given list. 
#  
# 
#  
# 
#  Example: 
# 
#  
# StreamChecker streamChecker = new StreamChecker(["cd","f","kl"]); // init the 
# dictionary.
# streamChecker.query('a');          // return false
# streamChecker.query('b');          // return false
# streamChecker.query('c');          // return false
# streamChecker.query('d');          // return true, because 'cd' is in the word
# list
# streamChecker.query('e');          // return false
# streamChecker.query('f');          // return true, because 'f' is in the wordl
# ist
# streamChecker.query('g');          // return false
# streamChecker.query('h');          // return false
# streamChecker.query('i');          // return false
# streamChecker.query('j');          // return false
# streamChecker.query('k');          // return false
# streamChecker.query('l');          // return true, because 'kl' is in the word
# list
#  
# 
#  
# 
#  Note: 
# 
#  
#  1 <= words.length <= 2000 
#  1 <= words[i].length <= 2000 
#  Words will only consist of lowercase English letters. 
#  Queries will only consist of lowercase English letters. 
#  The number of queries is at most 40000. 
#  
#  Related Topics Trie


# leetcode submit region begin(Prohibit modification and deletion)
class StreamChecker(object):

    def __init__(self, words):
        """
        :type words: List[str]
        """
        self.root = {}
        self.list = []
        for word in words:
            p = self.root
            for i in xrange(len(word) - 1, -1, -1):
                if word[i] not in p:
                    p[word[i]] = {}
                p = p[word[i]]
            p['#'] = None

    def query(self, letter):
        """
        :type letter: str
        :rtype: bool
        """
        self.list.append(letter)
        p = self.root
        for i in xrange(len(self.list) - 1, -1, -1):
            if self.list[i] not in p: return False
            p = p[self.list[i]]
            if '#' in p: return True
        return False
        


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
# leetcode submit region end(Prohibit modification and deletion)
