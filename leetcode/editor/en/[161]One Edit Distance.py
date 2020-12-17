#Given two strings s and t, determine if they are both one edit distance apart. 
#
# Note: 
#
# There are 3 possiblities to satisify one edit distance apart: 
#
# 
# Insert a character into s to get t 
# Delete a character from s to get t 
# Replace a character of s to get t 
# 
#
# Example 1: 
#
# 
#Input: s = "ab", t = "acb"
#Output: true
#Explanation: We can insert 'c' into s to get t.
# 
#
# Example 2: 
#
# 
#Input: s = "cab", t = "ad"
#Output: false
#Explanation: We cannot get t from s by only one step. 
#
# Example 3: 
#
# 
#Input: s = "1203", t = "1213"
#Output: true
#Explanation: We can replace '0' with '1' to get t. 
# Related Topics String



#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        m = len(s)
        n = len(t)
        if abs(m-n)>1: return False

        for i in range(min(m,n)):
            if s[i] != t[i]:
                if m>n: return s[i+1:]==t[i:]
                elif m<n: return s[i:]==t[i+1:]
                else: return s[i+1:]==t[i+1:]
        return abs(m-n)==1

    def isOneEditDistance2(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        m = len(s)
        n = len(t)
        if abs(m - n) > 1: return False
        count = 0
        i = 0
        j = 0
        while i < m and j < n:
            if s[i] != t[j]:
                count += 1
                if count == 2: return False
                if m > n:
                    i += 1
                elif m < n:
                    j += 1
                else:
                    i += 1
                    j += 1
            else:
                i += 1
                j += 1
        if i < m or j < n:
            count += 1
        return count==1
#leetcode submit region end(Prohibit modification and deletion)
