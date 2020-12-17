#Given two strings s and t, determine if they are isomorphic. 
#
# Two strings are isomorphic if the characters in s can be replaced to get t. 
#
# All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself. 
#
# Example 1: 
#
# 
#Input: s = "egg", t = "add"
#Output: true
# 
#
# Example 2: 
#
# 
#Input: s = "foo", t = "bar"
#Output: false 
#
# Example 3: 
#
# 
#Input: s = "paper", t = "title"
#Output: true 
#
# Note: 
#You may assume both s and t have the same length. 
# Related Topics Hash Table



#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        m = len(s)
        n = len(t)
        if m!=n: return False
        s2t = {}
        t2s = {}
        for i in range(m):
            if s[i] not in s2t: s2t[s[i]] = t[i]
            if t[i] not in t2s: t2s[t[i]] = s[i]
            if s2t[s[i]]!= t[i] or t2s[t[i]]!=s[i]: return False
        return True
#leetcode submit region end(Prohibit modification and deletion)
