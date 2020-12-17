# Given a non-empty string, encode the string such that its encoded length is th
# e shortest. 
# 
#  The encoding rule is: k[encoded_string], where the encoded_string inside the 
# square brackets is being repeated exactly k times. 
# 
#  Note: 
# 
#  
#  k will be a positive integer and encoded string will not be empty or have ext
# ra space. 
#  You may assume that the input string contains only lowercase English letters.
#  The string's length is at most 160. 
#  If an encoding process does not make the string shorter, then do not encode i
# t. If there are several solutions, return any of them is fine. 
#  
# 
#  
# 
#  Example 1: 
# 
#  
# Input: "aaa"
# Output: "aaa"
# Explanation: There is no way to encode it such that it is shorter than the inp
# ut string, so we do not encode it.
#  
# 
#  
# 
#  Example 2: 
# 
#  
# Input: "aaaaa"
# Output: "5[a]"
# Explanation: "5[a]" is shorter than "aaaaa" by 1 character.
#  
# 
#  
# 
#  Example 3: 
# 
#  
# Input: "aaaaaaaaaa"
# Output: "10[a]"
# Explanation: "a9[a]" or "9[a]a" are also valid solutions, both of them have th
# e same length = 5, which is the same as "10[a]".
#  
# 
#  
# 
#  Example 4: 
# 
#  
# Input: "aabcaabcd"
# Output: "2[aabc]d"
# Explanation: "aabc" occurs twice, so one answer can be "2[aabc]d".
#  
# 
#  
# 
#  Example 5: 
# 
#  
# Input: "abbbabbbcabbbabbbc"
# Output: "2[2[abbb]c]"
# Explanation: "abbbabbbc" occurs twice, but "abbbabbbc" can also be encoded to 
# "2[abbb]c", so one answer can be "2[2[abbb]c]".
#  
# 
#  
#  Related Topics Dynamic Programming


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def encode(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        dp = [[""]*n for _ in range(n)]
        for step in range(1, n+1):
            for i in range(n-step+1):
                j = i+step -1
                dp[i][j] = s[i:i+step]
                for k in range(i, j):
                    left = dp[i][k]
                    right = dp[k+1][j]
                    if len(left) + len(right) < len(dp[i][j]):
                        dp[i][j] = left + right
                t = s[i:i+step]
                replace = t
                pos = (t+t).find(t,1)
                if pos > 0:
                    replace = str(len(t)//pos) +'[%s]'%(dp[i][i+pos-1])
                if len(replace) < len(dp[i][j]): dp[i][j] = replace
        return dp[0][n-1]
# leetcode submit region end(Prohibit modification and deletion)
