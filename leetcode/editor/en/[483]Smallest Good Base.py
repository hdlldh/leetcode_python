# For an integer n, we call k>=2 a good base of n, if all digits of n base k are
#  1. 
# 
#  Now given a string representing n, you should return the smallest good base o
# f n in string format. 
# 
#  Example 1: 
# 
#  
# Input: "13"
# Output: "3"
# Explanation: 13 base 3 is 111.
#  
# 
#  
# 
#  Example 2: 
# 
#  
# Input: "4681"
# Output: "8"
# Explanation: 4681 base 8 is 11111.
#  
# 
#  
# 
#  Example 3: 
# 
#  
# Input: "1000000000000000000"
# Output: "999999999999999999"
# Explanation: 1000000000000000000 base 999999999999999999 is 11.
#  
# 
#  
# 
#  Note: 
# 
#  
#  The range of n is [3, 10^18]. 
#  The string representing n is always valid and will not have leading zeros. 
#  
# 
#  
#  Related Topics Math Binary Search


# leetcode submit region begin(Prohibit modification and deletion)
import math
class Solution(object):
    def smallestGoodBase(self, n):
        """
        :type n: str
        :rtype: str
        """
        mx = int(math.log(int(n)+1)/math.log(2))
        eps = 1e-6
        for m in range(mx, 1, -1):
            left = 2
            right = int(n)-2
            while left <= right:
                mid = (left + right) // 2
                sm = (mid ** m - 1) / (mid -1)
                diff = sm - int(n)
                if diff > eps:
                    right = mid -1
                elif diff < -eps:
                    left = mid +1
                else: return str(mid)
        return str(int(n)-1)
        
# leetcode submit region end(Prohibit modification and deletion)
