#Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, add spaces in s to construct a sentence where each word is a valid dictionary word. Return all such possible sentences. 
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
#Input:
#s = "catsanddog"
#wordDict = ["cat", "cats", "and", "sand", "dog"]
#Output:
#[
#  "cats and dog",
#  "cat sand dog"
#]
# 
#
# Example 2: 
#
# 
#Input:
#s = "pineapplepenapple"
#wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
#Output:
#[
#  "pine apple pen apple",
#  "pineapple pen apple",
#  "pine applepen apple"
#]
#Explanation: Note that you are allowed to reuse a dictionary word.
# 
#
# Example 3: 
#
# 
#Input:
#s = "catsandog"
#wordDict = ["cats", "dog", "sand", "and", "cat"]
#Output:
#[] 
# Related Topics Dynamic Programming Backtracking



#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):

    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """

        if not wordDict: return []
        mem = {}

        def dfs(s, wordDict, mem):
            if s in mem: return mem[s]
            if not s: return [""]
            out = []
            for word in wordDict:
                if len(word)<=len(s) and word==s[:len(word)]:
                    rem = dfs(s[len(word):], wordDict, mem)
                    for string in rem:
                        if string: out.append(word+" "+string)
                        else: out.append(word)
            mem[s] = out[:]
            return out
        dfs(s, wordDict, mem)
        return mem[s]


        
#leetcode submit region end(Prohibit modification and deletion)
