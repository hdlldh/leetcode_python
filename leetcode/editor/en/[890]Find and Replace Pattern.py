# You have a list of words and a pattern, and you want to know which words in wo
# rds matches the pattern. 
# 
#  A word matches the pattern if there exists a permutation of letters p so that
#  after replacing every letter x in the pattern with p(x), we get the desired wor
# d. 
# 
#  (Recall that a permutation of letters is a bijection from letters to letters:
#  every letter maps to another letter, and no two letters map to the same letter.
# ) 
# 
#  Return a list of the words in words that match the given pattern. 
# 
#  You may return the answer in any order. 
# 
#  
# 
#  
#  Example 1: 
# 
#  
# Input: words = ["abc","deq","mee","aqq","dkd","ccc"], pattern = "abb"
# Output: ["mee","aqq"]
# Explanation: "mee" matches the pattern because there is a permutation {a -> m,
#  b -> e, ...}. 
# "ccc" does not match the pattern because {a -> c, b -> c, ...} is not a permut
# ation,
# since a and b map to the same letter. 
# 
#  
# 
#  Note: 
# 
#  
#  1 <= words.length <= 50 
#  1 <= pattern.length = words[i].length <= 20 
#  
#  
#  Related Topics String


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """
        n = len(pattern)
        ans = []
        for word in words:
            w2p = {}
            p2w = {}
            i = 0
            while i<n:
                w = word[i]
                p = pattern[i]
                if w in w2p and w2p[w]!=p: break
                w2p[w] = p
                if p in p2w and p2w[p]!=w: break
                p2w[p] = w
                i+=1
            if i==n: ans.append(word)
        return ans

        
# leetcode submit region end(Prohibit modification and deletion)
