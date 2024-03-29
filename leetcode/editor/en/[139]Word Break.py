#Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words. 
#
# Note: 
#
# 
# The same word in the dictionary may be reused multiple times in the segmentation. 
# You may assume the dictionary does not contain duplicate words. 
# 
#
# Example 1: 
#
# 
#Input: s = "leetcode", wordDict = ["leet", "code"]
#Output: true
#Explanation: Return true because "leetcode" can be segmented as "leet code".
# 
#
# Example 2: 
#
# 
#Input: s = "applepenapple", wordDict = ["apple", "pen"]
#Output: true
#Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
#             Note that you are allowed to reuse a dictionary word.
# 
#
# Example 3: 
#
# 
#Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
#Output: false
# 
# Related Topics Dynamic Programming



#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        wordSet = set(wordDict)
        n = len(s)
        dp = [False]*(n+1)
        dp[0] = True
        for i in range(1, n+1):
            for j in range(i):
                if dp[j] and s[j:i] in wordSet: dp[i] =True
        return dp[-1]
        
#leetcode submit region end(Prohibit modification and deletion)
