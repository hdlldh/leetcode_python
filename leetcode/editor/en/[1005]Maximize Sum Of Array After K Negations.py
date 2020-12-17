# Given an array A of integers, we must modify the array in the following way: w
# e choose an i and replace A[i] with -A[i], and we repeat this process K times in
#  total. (We may choose the same index i multiple times.) 
# 
#  Return the largest possible sum of the array after modifying it in this way. 
# 
# 
#  
# 
#  Example 1: 
# 
#  
# Input: A = [4,2,3], K = 1
# Output: 5
# Explanation: Choose indices (1,) and A becomes [4,-2,3].
#  
# 
#  
#  Example 2: 
# 
#  
# Input: A = [3,-1,0,2], K = 3
# Output: 6
# Explanation: Choose indices (1, 2, 2) and A becomes [3,1,0,2].
#  
# 
#  
#  Example 3: 
# 
#  
# Input: A = [2,-3,-1,5,-4], K = 2
# Output: 13
# Explanation: Choose indices (1, 4) and A becomes [2,3,-1,5,4].
#  
#  
#  
# 
#  
# 
#  Note: 
# 
#  
#  1 <= A.length <= 10000 
#  1 <= K <= 10000 
#  -100 <= A[i] <= 100 
#  
#  Related Topics Greedy


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def largestSumAfterKNegations(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        pos = []
        neg = []
        for num in A:
            if num>=0: heapq.heappush(pos, num)
            else: heapq.heappush(neg, num)
        while K:
            if neg:
                num = heapq.heappop(neg)
                heapq.heappush(pos, -num)
            else:
                num = heapq.heappop(pos)
                if num > 0:
                    heapq.heappush(neg, -num)
                else:
                    heapq.heappush(pos, num)
            K -= 1
        return sum(pos) +sum(neg)
        
# leetcode submit region end(Prohibit modification and deletion)
