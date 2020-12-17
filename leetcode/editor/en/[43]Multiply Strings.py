#Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string. 
#
# Example 1: 
#
# 
#Input: num1 = "2", num2 = "3"
#Output: "6" 
#
# Example 2: 
#
# 
#Input: num1 = "123", num2 = "456"
#Output: "56088"
# 
#
# Note: 
#
# 
# The length of both num1 and num2 is < 110. 
# Both num1 and num2 contain only digits 0-9. 
# Both num1 and num2 do not contain any leading zero, except the number 0 itself. 
# You must not use any built-in BigInteger library or convert the inputs to integer directly. 
# 
# Related Topics Math String



#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        m = len(num1)
        n = len(num2)
        num1 = num1[::-1]
        num2 = num2[::-1]
        vals = [0]* (m+n)
        for i in range(m):
            for j in range(n):
                mul = (ord(num1[i])-ord('0')) *(ord(num2[j])-ord('0'))
                p1= i+j
                p2 = p1+1
                s = mul + vals[p1]
                vals[p2] += s//10
                vals[p1] = s%10
        vals.reverse()
        ans = ''.join([str(v) for v in vals])
        ans = ans.lstrip('0')
        if not ans: return "0"
        return ans
#leetcode submit region end(Prohibit modification and deletion)
