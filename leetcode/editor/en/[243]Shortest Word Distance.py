#Given a list of words and two words word1 and word2, return the shortest distance between these two words in the list. 
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
#
# Note: 
#You may assume that word1 does not equal to word2, and word1 and word2 are both in the list. 
# Related Topics Array



#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def shortestDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        i = -1
        j = -1
        ans = float('inf')
        for idx, word in enumerate(words):
            if word == word1:
                if j != -1: ans = min(ans, idx - j)
                i = idx
            elif word == word2:
                if i != -1: ans = min(ans, idx - i)
                j = idx
        return ans
#leetcode submit region end(Prohibit modification and deletion)
