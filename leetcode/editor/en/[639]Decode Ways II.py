# 
# A message containing letters from A-Z is being encoded to numbers using the fo
# llowing mapping way:
#  
# 
#  
# 'A' -> 1
# 'B' -> 2
# ...
# 'Z' -> 26
#  
# 
#  
# Beyond that, now the encoded string can also contain the character '*', which 
# can be treated as one of the numbers from 1 to 9.
#  
# 
# 
#  
# Given the encoded message containing digits and the character '*', return the 
# total number of ways to decode it.
#  
# 
#  
# Also, since the answer may be very large, you should return the output mod 109
#  + 7.
#  
# 
#  Example 1: 
#  
# Input: "*"
# Output: 9
# Explanation: The encoded message can be decoded to the string: "A", "B", "C", 
# "D", "E", "F", "G", "H", "I".
#  
#  
# 
#  Example 2: 
#  
# Input: "1*"
# Output: 9 + 9 = 18
#  
#  
# 
#  Note: 
#  
#  The length of the input string will fit in range [1, 105]. 
#  The input string will only contain the character '*' and digits '0' - '9'. 
#  
#  Related Topics Dynamic Programming


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        dp = [0]*(n+1)
        dp[0] = 1
        kmod = 1000000007
        if s[0] == '*': dp[1] = 9
        elif s[0] == '0': dp[1] = 0
        else: dp[1] = 1
        for i in range(1,n):
            c1 = self.helper1(s[i])
            c2 = self.helper2(s[i-1], s[i])

            dp[i+1] = (dp[i] * c1 + dp[i-1] * c2) % kmod
            #print(c1, c2, dp)
        return dp[n]

    def helper1(self, ch1):
        if ch1 =='0': return 0
        if ch1 =='*': return 9
        return 1

    def helper2(self, ch1, ch2):
        if ch1=='*' and ch2=='*': return 15
        if ch1=='*':
            if ch2>= '0' and ch2 <='6': return 2
            else: return 1
        if ch2 == '*':
            if ch1 == '1': return 9
            elif ch1 == '2': return 6
            else: return 0
        if ch1+ch2>='10' and ch1+ch2<='26': return 1
        return 0
        
# leetcode submit region end(Prohibit modification and deletion)
