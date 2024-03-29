#Design a class which receives a list of words in the constructor, and implements a method that takes two words word1 and word2 and return the shortest distance between these two words in the list. Your method will be called repeatedly many times with different parameters. 
#
# Example: 
#Assume that words = ["practice", "makes", "perfect", "coding", "makes"]. 
#
# 
#Input: word1 = “coding”, word2 = “practice”
#Output: 3
# 
#
# 
#Input: word1 = "makes", word2 = "coding"
#Output: 1 
#
# Note: 
#You may assume that word1 does not equal to word2, and word1 and word2 are both in the list. 
# Related Topics Hash Table Design



#leetcode submit region begin(Prohibit modification and deletion)
from collections import defaultdict
class WordDistance(object):

    def __init__(self, words):
        """
        :type words: List[str]
        """
        self.locations = defaultdict(list)
        for i, word in enumerate(words):
            self.locations[word].append(i)

    def shortest(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        l1 = self.locations[word1]
        l2 = self.locations[word2]
        m = len(l1)
        n = len(l2)
        i = 0
        j = 0
        ans = float('inf')
        while i<m and j<n:
            if l1[i] > l2[j]:
                ans = min(ans,l1[i]-l2[j])
                j+=1
            else:
                ans = min(ans, l2[j]-l1[i])
                i+=1
        return ans



# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(words)
# param_1 = obj.shortest(word1,word2)
#leetcode submit region end(Prohibit modification and deletion)
