#Given an integer n, count the total number of digit 1 appearing in all non-negative integers less than or equal to n. 
#
# Example: 
#
# 
#Input: 13
#Output: 6 
#Explanation: Digit 1 occurred in the following numbers: 1, 10, 11, 12, 13.
# 
# Related Topics Math



#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """
        i = 1
        ans = 0
        while i<=n:
            divider = i*10
            ans += (n//divider)*i + min(max(n%divider - i + 1, 0), i)
            i *= 10
        return ans
#leetcode submit region end(Prohibit modification and deletion)
