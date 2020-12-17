#Given two strings s and t , write a function to determine if t is an anagram of s. 
#
# Example 1: 
#
# 
#Input: s = "anagram", t = "nagaram"
#Output: true
# 
#
# Example 2: 
#
# 
#Input: s = "rat", t = "car"
#Output: false
# 
#
# Note: 
#You may assume the string contains only lowercase alphabets. 
#
# Follow up: 
#What if the inputs contain unicode characters? How would you adapt your solution to such case? 
# Related Topics Hash Table Sort



#leetcode submit region begin(Prohibit modification and deletion)
from collections import defaultdict
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return collections.Counter(s) == collections.Counter(t)

    def isAnagram2(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        m = len(s)
        n = len(t)
        if m!=n: return False
        hmap = defaultdict(int)
        for i in range(m):
            hmap[s[i]] += 1
            hmap[t[i]] -= 1

        for k, v in hmap.items():
            if v!=0: return False
        return True
        
#leetcode submit region end(Prohibit modification and deletion)
