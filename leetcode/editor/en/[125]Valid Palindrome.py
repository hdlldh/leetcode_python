#Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases. 
#
# Note: For the purpose of this problem, we define empty string as valid palindrome. 
#
# Example 1: 
#
# 
#Input: "A man, a plan, a canal: Panama"
#Output: true
# 
#
# Example 2: 
#
# 
#Input: "race a car"
#Output: false
# 
# Related Topics Two Pointers String



#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        n = len(s)
        if n==0: return True
        i = 0
        j = n-1
        s = s.lower()
        while i<j:
            while i<j and not (ord('a')<=ord(s[i]) <= ord('z') or ord('0')<=ord(s[i]) <= ord('9')):
                i+=1
            while i<j and not (ord('a')<=ord(s[j]) <= ord('z') or ord('0')<=ord(s[j]) <= ord('9')):
                j-=1
            if i<j and s[i]!=s[j]:return False
            i+=1
            j-=1
        return True



#leetcode submit region end(Prohibit modification and deletion)
