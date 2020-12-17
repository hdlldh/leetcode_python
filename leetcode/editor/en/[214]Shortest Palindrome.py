#Given a string s, you are allowed to convert it to a palindrome by adding characters in front of it. Find and return the shortest palindrome you can find by performing this transformation. 
#
# Example 1: 
#
# 
#Input: "aacecaaa"
#Output: "aaacecaaa"
# 
#
# Example 2: 
#
# 
#Input: "abcd"
#Output: "dcbabcd" Related Topics String



#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        revS = s[::-1]
        n = len(s)
        for i in range(n):
            if s[:n-i] == revS[i:]: return revS[:i] + s
        return ""
#leetcode submit region end(Prohibit modification and deletion)
