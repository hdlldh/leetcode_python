#Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters. 
#
# This is case sensitive, for example "Aa" is not considered a palindrome here. 
#
# Note: 
#Assume the length of given string will not exceed 1,010.
# 
#
# Example: 
# 
#Input:
#"abccccdd"
#
#Output:
#7
#
#Explanation:
#One longest palindrome that can be built is "dccaccd", whose length is 7.
# 
# Related Topics Hash Table



#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        c = collections.Counter(s)
        l = 0
        for k in c:
            l += (c[k] // 2) * 2
        return min(len(s), l + 1)
#leetcode submit region end(Prohibit modification and deletion)
