# Return all non-negative integers of length N such that the absolute difference
#  between every two consecutive digits is K. 
# 
#  Note that every number in the answer must not have leading zeros except for t
# he number 0 itself. For example, 01 has one leading zero and is invalid, but 0 i
# s valid. 
# 
#  You may return the answer in any order. 
# 
#  
# 
#  Example 1: 
# 
#  
# Input: N = 3, K = 7
# Output: [181,292,707,818,929]
# Explanation: Note that 070 is not a valid number, because it has leading zeroe
# s.
#  
# 
#  
#  Example 2: 
# 
#  
# Input: N = 2, K = 1
# Output: [10,12,21,23,32,34,43,45,54,56,65,67,76,78,87,89,98] 
# 
#  
#  
# 
#  Note: 
# 
#  
#  1 <= N <= 9 
#  0 <= K <= 9 
#  
#  Related Topics Dynamic Programming


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def numsSameConsecDiff(self, N, K):
        """
        :type N: int
        :type K: int
        :rtype: List[int]
        """
        ans = []
        if N == 1: ans.append(0)
        for i in range(1, 10):
            self.dfs(N-1, K, i, ans)
        return ans

    def dfs(self, n, K, curr, ans):
        if n==0:
            ans.append(curr)
            return
        l = curr % 10
        if l+K<10: self.dfs(n-1, K, curr*10+l+K, ans)
        if l-K>=0 and K!=0: self.dfs(n-1, K, curr*10+l-K, ans)



        
# leetcode submit region end(Prohibit modification and deletion)
