# Given two strings str1 and str2 of the same length, determine whether you can 
# transform str1 into str2 by doing zero or more conversions. 
# 
#  In one conversion you can convert all occurrences of one character in str1 to
#  any other lowercase English character. 
# 
#  Return true if and only if you can transform str1 into str2. 
# 
#  
# 
#  Example 1: 
# 
#  
# Input: str1 = "aabcc", str2 = "ccdee"
# Output: true
# Explanation: Convert 'c' to 'e' then 'b' to 'd' then 'a' to 'c'. Note that the
#  order of conversions matter.
#  
# 
#  Example 2: 
# 
#  
# Input: str1 = "leetcode", str2 = "codeleet"
# Output: false
# Explanation: There is no way to transform str1 to str2.
#  
# 
#  
# 
#  Note: 
# 
#  
#  1 <= str1.length == str2.length <= 10^4 
#  Both str1 and str2 contain only lowercase English letters. 
#  
#  Related Topics Graph


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def canConvert(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: bool
        """
        if str1 == str2: return True
        graph = {}
        for i, ch in enumerate(str1):
            if ch not in graph:
                graph[ch] = str2[i]
            else:
                if graph[ch] != str2[i]: return False

        if len(set(str2)) == 26: return False
        return True
        
# leetcode submit region end(Prohibit modification and deletion)
