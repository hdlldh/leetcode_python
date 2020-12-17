# You are given an array x of n positive numbers. You start at point (0,0) and m
# oves x[0] metres to the north, then x[1] metres to the west, x[2] metres to the 
# south, x[3] metres to the east and so on. In other words, after each move your d
# irection changes counter-clockwise. 
# 
#  Write a one-pass algorithm with O(1) extra space to determine, if your path c
# rosses itself, or not. 
# 
#  
# 
#  Example 1: 
# 
#  
# ┌───┐
# │   │
# └───┼──>
#     │
# 
# Input: [2,1,1,2]
# Output: true
#  
# 
#  Example 2: 
# 
#  
# ┌──────┐
# │      │
# │
# │
# └────────────>
# 
# Input: [1,2,3,4]
# Output: false 
#  
# 
#  Example 3: 
# 
#  
# ┌───┐
# │   │
# └───┼>
# 
# Input: [1,1,1,1]
# Output: true 
#  
#  Related Topics Math


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def isSelfCrossing(self, x):
        """
        :type x: List[int]
        :rtype: bool
        """
        n = len(x)
        if n<=3: return False

        for i in range(3, n):
            if x[i-3] >= x[i-1] and x[i-2] <=x[i]: return True
            if i>=4 and x[i-4]+x[i]>=x[i-2] and x[i-3]==x[i-1]: return True
            if i>=5 and x[i-5]<=x[i-3] and x[i]<=x[i-2] and x[i-1]<=x[i-3] \
                    and x[i-4]<=x[i-2] and x[i-1]>=x[i-3]-x[i-5] \
                    and x[i]>=x[i-2]-x[i-4]: return True

        return False
# leetcode submit region end(Prohibit modification and deletion)
