# 
# Given a string and a string dictionary, find the longest string in the diction
# ary that can be formed by deleting some characters of the given string. If there
#  are more than one possible results, return the longest word with the smallest l
# exicographical order. If there is no possible result, return the empty string.
#  
#  Example 1: 
#  
# Input:
# s = "abpcplea", d = ["ale","apple","monkey","plea"]
# 
# Output: 
# "apple"
#  
#  
# 
#  
#  Example 2: 
#  
# Input:
# s = "abpcplea", d = ["a","b","c"]
# 
# Output: 
# "a"
#  
#  
# 
#  Note: 
#  
#  All the strings in the input will only contain lower-case letters. 
#  The size of the dictionary won't exceed 1,000. 
#  The length of all the strings in the input won't exceed 1,000. 
#  
#  Related Topics Two Pointers Sort


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def findLongestWord(self, s, d):
        """
        :type s: str
        :type d: List[str]
        :rtype: str
        """
        d.sort(key=lambda x: (-len(x), x))
        for word in d:
            if self.canRemove(s, word): return word
        return ""

    def canRemove(self, s, word):
        n = len(word)
        i = 0
        for ch in s:
            if i<n and ch == word[i]: i += 1
        return i==n
# leetcode submit region end(Prohibit modification and deletion)
