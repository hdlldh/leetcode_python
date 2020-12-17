#Given two binary strings, return their sum (also a binary string). 
#
# The input strings are both non-empty and contains only characters 1 or 0. 
#
# Example 1: 
#
# 
#Input: a = "11", b = "1"
#Output: "100" 
#
# Example 2: 
#
# 
#Input: a = "1010", b = "1011"
#Output: "10101" 
# Related Topics Math String



#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a1 = a[::-1]
        b1 = b[::-1]
        n = len(a1)
        m = len(b1)
        ci = 0
        i = 0
        ans = ''
        while i< m or i<n:
            s = 0
            if i<n: s += ord(a1[i]) - ord('0')
            if i<m: s += ord(b1[i]) - ord('0')
            s += ci
            ci = 1 if s >=2 else 0
            ans += str(s%2)
            i += 1
        if ci==1: ans +='1'
        ans = ans[::-1]
        return ans



        
#leetcode submit region end(Prohibit modification and deletion)
