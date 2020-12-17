#Given a list of words and two words word1 and word2, return the shortest distance between these two words in the list. 
#
# word1 and word2 may be the same and they represent two individual words in the list. 
#
# Example: 
#Assume that words = ["practice", "makes", "perfect", "coding", "makes"]. 
#
# 
#Input: word1 = “makes”, word2 = “coding”
#Output: 1
# 
#
# 
#Input: word1 = "makes", word2 = "makes"
#Output: 3
# 
#
# Note: 
#You may assume word1 and word2 are both in the list. 
# Related Topics Array



#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def shortestWordDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        i = -1
        ans = float('inf')
        n = len(words)
        if word1 == word2:
            j = 0
            while j<n:
                if words[j] == word1:
                    if i!= -1: ans = min(ans, j-i)
                    i = j
                j+=1
        else:
            j = -1
            k = 0
            while k<n:
                if words[k] == word1:
                    if j!=-1: ans = min(ans, k-j)
                    i = k
                if words[k] == word2:
                    if i!=-1: ans = min(ans, k-i)
                    j = k
                k += 1
        return ans
#leetcode submit region end(Prohibit modification and deletion)
