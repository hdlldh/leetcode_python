#Given a string s1, we may represent it as a binary tree by partitioning it to two non-empty substrings recursively. 
#
# Below is one possible representation of s1 = "great": 
#
# 
#    great
#   /    \
#  gr    eat
# / \    /  \
#g   r  e   at
#           / \
#          a   t
# 
#
# To scramble the string, we may choose any non-leaf node and swap its two children. 
#
# For example, if we choose the node "gr" and swap its two children, it produces a scrambled string "rgeat". 
#
# 
#    rgeat
#   /    \
#  rg    eat
# / \    /  \
#r   g  e   at
#           / \
#          a   t
# 
#
# We say that "rgeat" is a scrambled string of "great". 
#
# Similarly, if we continue to swap the children of nodes "eat" and "at", it produces a scrambled string "rgtae". 
#
# 
#    rgtae
#   /    \
#  rg    tae
# / \    /  \
#r   g  ta  e
#       / \
#      t   a
# 
#
# We say that "rgtae" is a scrambled string of "great". 
#
# Given two strings s1 and s2 of the same length, determine if s2 is a scrambled string of s1. 
#
# Example 1: 
#
# 
#Input: s1 = "great", s2 = "rgeat"
#Output: true
# 
#
# Example 2: 
#
# 
#Input: s1 = "abcde", s2 = "caebd"
#Output: false 
# Related Topics String Dynamic Programming



#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if s1 == s2: return True
        ss1 = ''.join(sorted(s1))
        ss2 = ''.join(sorted(s2))
        if ss1!=ss2: return False
        n = len(s1)
        for i in range(1, n):
            s11 = s1[:i]
            s12 = s1[i:]
            s21 = s2[:i]
            s22 = s2[i:]
            if self.isScramble(s11,s21) and self.isScramble(s12, s22): return True
            s21 = s2[-i:]
            s22 = s2[:-i]
            if self.isScramble(s11, s21) and self.isScramble(s12, s22): return True
        return False
        
#leetcode submit region end(Prohibit modification and deletion)
