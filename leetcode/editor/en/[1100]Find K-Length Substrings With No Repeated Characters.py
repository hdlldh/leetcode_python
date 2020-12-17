# Given a string S, return the number of substrings of length K with no repeated
#  characters. 
# 
#  
# 
#  Example 1: 
# 
#  
# Input: S = "havefunonleetcode", K = 5
# Output: 6
# Explanation: 
# There are 6 substrings they are : 'havef','avefu','vefun','efuno','etcod','tco
# de'.
#  
# 
#  Example 2: 
# 
#  
# Input: S = "home", K = 5
# Output: 0
# Explanation: 
# Notice K can be larger than the length of S. In this case is not possible to f
# ind any substring.
#  
# 
#  
# 
#  Note: 
# 
#  
#  1 <= S.length <= 10^4 
#  All characters of S are lowercase English letters. 
#  1 <= K <= 10^4 
#  
#  Related Topics String Sliding Window


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def numKLenSubstrNoRepeats(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: int
        """
        n = len(S)
        if K > n: return 0

        i = 0
        mem = dict()
        ans = 0
        while i < n:
            if i >= K:
                if S[i - K] in mem and mem[S[i - K]] == i - K: mem.pop(S[i - K])
            if S[i] not in mem:
                mem[S[i]] = i
                i += 1
            else:
                j = mem[S[i]]
                for k, v in mem.items():
                    if v <= j: mem.pop(k)
                mem[S[i]] = i
                i += 1
            if len(mem) == K: ans += 1
        return ans
        
# leetcode submit region end(Prohibit modification and deletion)
