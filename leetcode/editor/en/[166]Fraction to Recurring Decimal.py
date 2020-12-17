#Given two integers representing the numerator and denominator of a fraction, return the fraction in string format. 
#
# If the fractional part is repeating, enclose the repeating part in parentheses. 
#
# Example 1: 
#
# 
#Input: numerator = 1, denominator = 2
#Output: "0.5"
# 
#
# Example 2: 
#
# 
#Input: numerator = 2, denominator = 1
#Output: "2" 
#
# Example 3: 
#
# 
#Input: numerator = 2, denominator = 3
#Output: "0.(6)"
# 
# Related Topics Hash Table Math



#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        s1 = 1 if numerator >=0 else -1
        s2 = 1 if denominator>=0 else -1
        numerator = -numerator if numerator <0 else numerator
        denominator = -denominator if denominator<0 else denominator
        q, r = divmod(numerator, denominator)
        ans = str(q)
        if s1*s2==-1 and (q>0 or r>0) : ans= '-'+ans
        if r==0: return ans
        ans += '.'
        m = {}
        pos = 0
        s = ""
        while r:
            if r in m:
                s = s[:m[r]]+'('+s[m[r]:]+')'
                return ans+s
            m[r] = pos
            pos += 1
            q, r = divmod(r*10, denominator)
            s += str(q)
        return ans+s
        
#leetcode submit region end(Prohibit modification and deletion)
