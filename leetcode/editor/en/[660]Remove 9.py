# Start from integer 1, remove any integer that contains 9 such as 9, 19, 29... 
# 
# 
#  So now, you will have a new integer sequence: 1, 2, 3, 4, 5, 6, 7, 8, 10, 11,
#  ... 
# 
#  Given a positive integer n, you need to return the n-th integer after removin
# g. Note that 1 will be the first integer. 
# 
#  Example 1: 
#  
# Input: 9
# Output: 10
#  
#  
# 
#  
#  Hint: n will not exceed 9 x 10^8.
#  Related Topics Math


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def newInteger(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans = []
        while n:
            ans.append(n%9)
            n = n//9
        val = 0
        ans.reverse()
        for p in ans:
            val = val*10+p
        return val
# leetcode submit region end(Prohibit modification and deletion)
