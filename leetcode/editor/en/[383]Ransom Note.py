#
#Given an arbitrary ransom note string and another string containing letters from all the magazines, write a function that will return true if the ransom 
#note can be constructed from the magazines ; otherwise, it will return false. 
# 
# 
#Each letter in the magazine string can only be used once in your ransom note.
# 
#
# Note: 
#You may assume that both strings contain only lowercase letters.
# 
#
# 
#canConstruct("a", "b") -> false
#canConstruct("aa", "ab") -> false
#canConstruct("aa", "aab") -> true
# 
# Related Topics String



#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        
#leetcode submit region end(Prohibit modification and deletion)
