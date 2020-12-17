#Given a non-negative integer num represented as a string, remove k digits from the number so that the new number is the smallest possible.
# 
#
# Note: 
# 
# The length of num is less than 10002 and will be ≥ k. 
# The given num does not contain any leading zero. 
# 
#
# 
#
# Example 1:
# 
#Input: num = "1432219", k = 3
#Output: "1219"
#Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.
# 
# 
#
# Example 2:
# 
#Input: num = "10200", k = 1
#Output: "200"
#Explanation: Remove the leading 1 and the number is 200. Note that the output must not contain leading zeroes.
# 
# 
#
# Example 3:
# 
#Input: num = "10", k = 2
#Output: "0"
#Explanation: Remove all the digits from the number and it is left with nothing which is 0.
# 
# Related Topics Stack Greedy



#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        n = len(num)
        stack = ""
        if k==n: return '0'
        keep = n-k
        for c in num:
            while k>0 and stack and c<stack[-1]:
                stack = stack[:-1]
                k -=1
            stack += c
        stack = stack[:keep]
        stack = stack.lstrip('0')
        if not stack: return '0'
        return stack
        
#leetcode submit region end(Prohibit modification and deletion)
