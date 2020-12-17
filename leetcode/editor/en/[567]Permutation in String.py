#Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1. In other words, one of the first string's permutations is the substring of the second string. 
#
# 
#
# Example 1: 
#
# 
#Input: s1 = "ab" s2 = "eidbaooo"
#Output: True
#Explanation: s2 contains one permutation of s1 ("ba").
# 
#
# Example 2: 
#
# 
#Input:s1= "ab" s2 = "eidboaoo"
#Output: False
# 
#
# 
#
# Note: 
#
# 
# The input strings only contain lower case letters. 
# The length of both given strings is in range [1, 10,000]. 
# 
# Related Topics Two Pointers Sliding Window



#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        m = len(s1)
        n = len(s2)
        if m>n: return False
        ref = {}
        hmap = {}
        for ch in s1:
            ref[ch] = ref.get(ch, 0) +1
        i = 0
        for i in range(m):
            ch = s2[i]
            hmap[ch] = hmap.get(ch,0) +1

        if hmap == ref: return True
        for i in range(m, n):
            ch = s2[i]
            hmap[ch] = hmap.get(ch, 0) + 1
            ch = s2[i-m]
            cnt = hmap[ch]
            if cnt ==1: del hmap[ch]
            else: hmap[ch] -= 1
            if hmap == ref: return True
        return False

        
#leetcode submit region end(Prohibit modification and deletion)
