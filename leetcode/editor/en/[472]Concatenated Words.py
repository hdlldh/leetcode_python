# Given a list of words (without duplicates), please write a program that return
# s all concatenated words in the given list of words.
#  A concatenated word is defined as a string that is comprised entirely of at l
# east two shorter words in the given array. 
# 
#  Example: 
#  
# Input: ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","
# ratcatdogcat"]
# 
# Output: ["catsdogcats","dogcatsdog","ratcatdogcat"]
# 
# Explanation: "catsdogcats" can be concatenated by "cats", "dog" and "cats";  "
# dogcatsdog" can be concatenated by "dog", "cats" and "dog"; "ratcatdogcat" can b
# e concatenated by "rat", "cat", "dog" and "cat".
#  
#  
# 
#  Note: 
#  
#  The number of elements of the given array will not exceed 10,000 
#  The length sum of elements in the given array will not exceed 600,000. 
#  All the input string will only include lower case letters. 
#  The returned elements order does not matter. 
#  
#  Related Topics Dynamic Programming Depth-first Search Trie


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def findAllConcatenatedWordsInADict(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """

        wordset = set(words)
        ans = []
        for word in words:
            wordset.remove(word)
            n = len(word)
            if n == 0: continue
            dp = [False] * (n + 1)
            dp[0] = True
            for i in range(n + 1):
                for j in range(i):
                    if dp[j] and word[j:i] in wordset:
                        dp[i] = True
                        break
            if dp[-1]: ans.append(word)
            wordset.add(word)
        return ans
        
# leetcode submit region end(Prohibit modification and deletion)
