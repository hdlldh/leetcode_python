# For some fixed N, an array A is beautiful if it is a permutation of the intege
# rs 1, 2, ..., N, such that: 
# 
#  For every i < j, there is no k with i < k < j such that A[k] * 2 = A[i] + A[j
# ]. 
# 
#  Given N, return any beautiful array A. (It is guaranteed that one exists.) 
# 
#  
# 
#  Example 1: 
# 
#  
# Input: 4
# Output: [2,1,4,3]
#  
# 
#  
#  Example 2: 
# 
#  
# Input: 5
# Output: [3,1,2,5,4] 
# 
#  
#  
# 
#  Note: 
# 
#  
#  1 <= N <= 1000 
#  
# 
#  
#  
#  Related Topics Divide and Conquer


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def beautifulArray(self, N):
        """
        :type N: int
        :rtype: List[int]
        """
        ans = [1]
        while len(ans) <N:
            t = []
            for num in ans:
                if 2*num-1<=N: t.append(2*num-1)
            for num in ans:
                if 2*num<=N: t.append(2*num)
            ans = t
        return ans
        
# leetcode submit region end(Prohibit modification and deletion)
