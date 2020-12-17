# Return the length of the shortest, non-empty, contiguous subarray of A with su
# m at least K. 
# 
#  If there is no non-empty subarray with sum at least K, return -1. 
# 
#  
# 
#  
#  
# 
#  
#  Example 1: 
# 
#  
# Input: A = [1], K = 1
# Output: 1
#  
# 
#  
#  Example 2: 
# 
#  
# Input: A = [1,2], K = 4
# Output: -1
#  
# 
#  
#  Example 3: 
# 
#  
# Input: A = [2,-1,2], K = 3
# Output: 3
#  
# 
#  
# 
#  Note: 
# 
#  
#  1 <= A.length <= 50000 
#  -10 ^ 5 <= A[i] <= 10 ^ 5 
#  1 <= K <= 10 ^ 9 
#  
#  
#  
#  
#  Related Topics Binary Search Queue


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def shortestSubarray(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        n = len(A)
        hp = []
        s = 0
        ans = float('inf')
        for i, a in enumerate(A):
            s+=a
            if s>=K: ans = min(ans, i+1)
            while hp and s-hp[0][0]>=K:
                _, j = heapq.heappop(hp)
                ans = min(ans, i-j)
            heapq.heappush(hp,[s, i])
        return ans if ans < float('inf') else -1
        
# leetcode submit region end(Prohibit modification and deletion)
