# Given an integer n, return any array containing n unique integers such that th
# ey add up to 0. 
# 
#  
#  Example 1: 
# 
#  
# Input: n = 5
# Output: [-7,-1,1,3,4]
# Explanation: These arrays also are accepted [-5,-1,1,2,3] , [-3,-1,2,-2,4].
#  
# 
#  Example 2: 
# 
#  
# Input: n = 3
# Output: [-1,0,1]
#  
# 
#  Example 3: 
# 
#  
# Input: n = 1
# Output: [0]
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= n <= 1000 
#  Related Topics Array


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def sumZero(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        if n%2: return [i-n//2 for i in range(n)]
        return [i+1 for i in range(n//2)] + [-i-1 for i in range(n//2)]
        
# leetcode submit region end(Prohibit modification and deletion)
