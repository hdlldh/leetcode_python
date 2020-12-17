# A string of '0's and '1's is monotone increasing if it consists of some number
#  of '0's (possibly 0), followed by some number of '1's (also possibly 0.) 
# 
#  We are given a string S of '0's and '1's, and we may flip any '0' to a '1' or
#  a '1' to a '0'. 
# 
#  Return the minimum number of flips to make S monotone increasing. 
# 
#  
# 
#  
#  Example 1: 
# 
#  
# Input: "00110"
# Output: 1
# Explanation: We flip the last digit to get 00111.
#  
# 
#  
#  Example 2: 
# 
#  
# Input: "010110"
# Output: 2
# Explanation: We flip to get 011111, or alternatively 000111.
#  
# 
#  
#  Example 3: 
# 
#  
# Input: "00011000"
# Output: 2
# Explanation: We flip to get 00000000.
#  
# 
#  
# 
#  Note: 
# 
#  
#  1 <= S.length <= 20000 
#  S only consists of '0' and '1' characters. 
#  
#  
#  
#  Related Topics Array


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def minFlipsMonoIncr(self, S):
        """
        :type S: str
        :rtype: int
        """
        n = len(S)
        l = [0]*(n+1)
        r = [0]*(n+1)
        for i in range(1,n+1):
            l[i] = l[i-1] + (1 if S[i-1]=='1' else 0)
            r[i] = r[i-1] + (1 if S[n-i]=='0' else 0)

        ans = float('inf')
        for i in range(n+1):
            ans = min(ans, l[i] + r[n-i])
        return ans


# leetcode submit region end(Prohibit modification and deletion)
