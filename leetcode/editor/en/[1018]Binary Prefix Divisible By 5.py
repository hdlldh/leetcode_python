# Given an array A of 0s and 1s, consider N_i: the i-th subarray from A[0] to A[
# i] interpreted as a binary number (from most-significant-bit to least-significan
# t-bit.) 
# 
#  Return a list of booleans answer, where answer[i] is true if and only if N_i 
# is divisible by 5. 
# 
#  Example 1: 
# 
#  
# Input: [0,1,1]
# Output: [true,false,false]
# Explanation: 
# The input numbers in binary are 0, 01, 011; which are 0, 1, and 3 in base-10. 
#  Only the first number is divisible by 5, so answer[0] is true.
#  
# 
#  Example 2: 
# 
#  
# Input: [1,1,1]
# Output: [false,false,false]
#  
# 
#  Example 3: 
# 
#  
# Input: [0,1,1,1,1,1]
# Output: [true,false,false,false,true,false]
#  
# 
#  Example 4: 
# 
#  
# Input: [1,1,1,0,1]
# Output: [false,false,false,false,false]
#  
# 
#  
# 
#  Note: 
# 
#  
#  1 <= A.length <= 30000 
#  A[i] is 0 or 1 
#  
#  Related Topics Array


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def prefixesDivBy5(self, A):
        """
        :type A: List[int]
        :rtype: List[bool]
        """
        num = 0
        ans = []
        for a in A:
            num = num*2+a
            if num % 5==0: ans.append(True)
            else:ans.append(False)
        return ans
# leetcode submit region end(Prohibit modification and deletion)
