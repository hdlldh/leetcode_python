# Given an array of integers A, a move consists of choosing any A[i], and increm
# enting it by 1. 
# 
#  Return the least number of moves to make every value in A unique. 
# 
#  
# 
#  Example 1: 
# 
#  
# Input: [1,2,2]
# Output: 1
# Explanation:  After 1 move, the array could be [1, 2, 3].
#  
# 
#  
#  Example 2: 
# 
#  
# Input: [3,2,1,2,1,7]
# Output: 6
# Explanation:  After 6 moves, the array could be [3, 4, 1, 2, 5, 7].
# It can be shown with 5 or less moves that it is impossible for the array to ha
# ve all unique values.
#  
# 
#  
#  
# 
#  Note: 
# 
#  
#  0 <= A.length <= 40000 
#  0 <= A[i] < 40000 
#  
# 
#  
#  
#  Related Topics Array


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def minIncrementForUnique(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        count = collections.Counter(A)
        queue = collections.deque()
        ans = 0
        for x in xrange(100000):
            if count[x] >= 2:
                while count[x] >= 2:
                    queue.append(x)
                    count[x] -= 1
            elif queue and count[x] == 0:
                ans += x - queue.popleft()
        return ans
        
# leetcode submit region end(Prohibit modification and deletion)
