# Given an array of strings arr. String s is a concatenation of a sub-sequence o
# f arr which have unique characters. 
# 
#  Return the maximum possible length of s. 
# 
#  
#  Example 1: 
# 
#  
# Input: arr = ["un","iq","ue"]
# Output: 4
# Explanation: All possible concatenations are "","un","iq","ue","uniq" and "iqu
# e".
# Maximum length is 4.
#  
# 
#  Example 2: 
# 
#  
# Input: arr = ["cha","r","act","ers"]
# Output: 6
# Explanation: Possible solutions are "chaers" and "acters".
#  
# 
#  Example 3: 
# 
#  
# Input: arr = ["abcdefghijklmnopqrstuvwxyz"]
# Output: 26
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= arr.length <= 16 
#  1 <= arr[i].length <= 26 
#  arr[i] contains only lower case English letters. 
#  
#  Related Topics Backtracking Bit Manipulation


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def maxLength(self, arr):
        """
        :type arr: List[str]
        :rtype: int
        """
        N = len(arr)
        self.ans = 0

        self.helper(arr, N, 0, '')
        return self.ans

    def helper(self, arr, n, start, out):
        self.ans = max(self.ans, len(out))
        if start == n:
            return

        for i in range(start, n):
            if not self.is_unique(arr[i]): continue
            if self.is_overlapped(out, arr[i]): continue
            self.helper(arr, n, i + 1, out + arr[i])

    def is_overlapped(self, str1, str2):
        for ch in str1:
            if ch in str2: return True
        return False

    def is_unique(self, str1):
        count = collections.Counter(str1)
        for k, v in count.items():
            if v > 1: return False
        return True
        
# leetcode submit region end(Prohibit modification and deletion)
