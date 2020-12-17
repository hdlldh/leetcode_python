#Given a pattern and a string str, find if str follows the same pattern. 
#
# Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str. 
#
# Example 1: 
#
# 
#Input: pattern = "abba", str = "dog cat cat dog"
#Output: true 
#
# Example 2: 
#
# 
#Input:pattern = "abba", str = "dog cat cat fish"
#Output: false 
#
# Example 3: 
#
# 
#Input: pattern = "aaaa", str = "dog cat cat dog"
#Output: false 
#
# Example 4: 
#
# 
#Input: pattern = "abba", str = "dog dog dog dog"
#Output: false 
#
# Notes: 
#You may assume pattern contains only lowercase letters, and str contains lowercase letters that may be separated by a single space. 
# Related Topics Hash Table



#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def wordPattern2(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        num_pattern = len(pattern)
        str_list = str.split(' ')
        num_str = len(str_list)
        p2s = {}
        s2p = {}
        if num_pattern != num_str: return False
        for i in range(num_pattern):
            if pattern[i] not in p2s: p2s[pattern[i]] = str_list[i]
            if str_list[i] not in s2p: s2p[str_list[i]] = pattern[i]
            if p2s[pattern[i]] != str_list[i] or s2p[str_list[i]] != pattern[i]: return False
        return True

    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        str_list = str.split(' ')
        if len(pattern)!=len(str_list): return False
        p2s = {}
        s2p = {}
        for i in range(len(pattern)):
            if pattern[i] not in p2s and str_list[i] not in s2p:
                p2s[pattern[i]] = str_list[i]
                s2p[str_list[i]] = pattern[i]
            elif pattern[i] in p2s and str_list[i] in s2p:
                if p2s[pattern[i]] != str_list[i] or s2p[str_list[i]] != pattern[i]: return False
            else: return False
        return True

#leetcode submit region end(Prohibit modification and deletion)
