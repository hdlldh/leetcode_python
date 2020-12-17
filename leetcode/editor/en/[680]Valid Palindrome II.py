# 
# Given a non-empty string s, you may delete at most one character. Judge whethe
# r you can make it a palindrome.
#  
# 
#  Example 1: 
#  
# Input: "aba"
# Output: True
#  
#  
# 
#  Example 2: 
#  
# Input: "abca"
# Output: True
# Explanation: You could delete the character 'c'.
#  
#  
# 
#  Note: 
#  
#  The string will only contain lowercase characters a-z.
# The maximum length of the string is 50000. 
#  
#  Related Topics String


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        N = len(s)
        l =0
        r =N-1
        while l<r:
            if s[l]!=s[r]: return self.isPalindrome(s[l+1:r+1]) or self.isPalindrome(s[l:r])
            l+=1
            r-=1

        return True

    def isPalindrome(self, s):
        l = 0
        r = len(s)-1
        while l<r:
            if s[l]!=s[r]: return False
            l+=1
            r-=1
        return True
# leetcode submit region end(Prohibit modification and deletion)
