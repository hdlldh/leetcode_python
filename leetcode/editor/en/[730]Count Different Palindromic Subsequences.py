# 
# Given a string S, find the number of different non-empty palindromic subsequen
# ces in S, and return that number modulo 10^9 + 7.
#  
# A subsequence of a string S is obtained by deleting 0 or more characters from 
# S.
#  
# A sequence is palindromic if it is equal to the sequence reversed.
#  
# Two sequences A_1, A_2, ... and B_1, B_2, ... are different if there is some i
#  for which A_i != B_i.
#  
# 
#  Example 1: 
#  
# Input: 
# S = 'bccb'
# Output: 6
# Explanation: 
# The 6 different non-empty palindromic subsequences are 'b', 'c', 'bb', 'cc', '
# bcb', 'bccb'.
# Note that 'bcb' is counted only once, even though it occurs twice.
#  
#  
# 
#  Example 2: 
#  
# Input: 
# S = 'abcdabcdabcdabcdabcdabcdabcdabcddcbadcbadcbadcbadcbadcbadcbadcba'
# Output: 104860361
# Explanation: 
# There are 3104860382 different non-empty palindromic subsequences, which is 10
# 4860361 modulo 10^9 + 7.
#  
#  
# 
#  Note:
#  The length of S will be in the range [1, 1000]. 
#  Each character S[i] will be in the set {'a', 'b', 'c', 'd'}. 
#  Related Topics String Dynamic Programming


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def countPalindromicSubsequences(self, S):
        """
        :type S: str
        :rtype: int
        """
        n = len(S)
        mem = [0] * (n*n)
        return self.helper(S, 0, n-1, mem)

    def helper(self, S, start, end, mem):
        if start>end: return 0
        n = len(S)
        index = start * n + end
        if start==end:
            mem[index] = 1
            return 1

        if mem[index]>0: return mem[index]
        if S[start] == S[end]:
            l = start+1
            r = end -1
            while l<=r and S[l]!=S[start]: l+=1
            while l<=r and S[r]!=S[start]: r-=1
            if l>r: ans = 2*self.helper(S, start+1, end-1, mem)+2
            elif l==r: ans = 2*self.helper(S, start+1, end-1, mem)+1
            else: ans = 2*self.helper(S, start+1, end-1, mem)-self.helper(S, l+1, r-1, mem)
        else:
            ans = self.helper(S, start+1, end, mem) + self.helper(S, start, end-1, mem)\
                  - self.helper(S, start+1, end-1, mem)
        mem[index] = ans %1000000007
        return mem[index]

        
# leetcode submit region end(Prohibit modification and deletion)
