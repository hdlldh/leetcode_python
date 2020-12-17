# Given a string S, find out the length of the longest repeating substring(s). R
# eturn 0 if no repeating substring exists. 
# 
#  
# 
#  Example 1: 
# 
#  
# Input: "abcd"
# Output: 0
# Explanation: There is no repeating substring.
#  
# 
#  Example 2: 
# 
#  
# Input: "abbaba"
# Output: 2
# Explanation: The longest repeating substrings are "ab" and "ba", each of which
#  occurs twice.
#  
# 
#  Example 3: 
# 
#  
# Input: "aabcaabdaab"
# Output: 3
# Explanation: The longest repeating substring is "aab", which occurs 3 times.
#  
# 
#  Example 4: 
# 
#  
# Input: "aaaaa"
# Output: 4
# Explanation: The longest repeating substring is "aaaa", which occurs twice.
#  
# 
#  
# 
#  Note: 
# 
#  
#  The string S consists of only lowercase English letters from 'a' - 'z'. 
#  1 <= S.length <= 1500 
#  Related Topics String


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def longestRepeatingSubstring(self, S):
        """
        :type S: str
        :rtype: int
        """

        N = len(S)
        low = 1
        high = N
        while low <= high:
            mid = low + (high - low) // 2
            if not self.hasRepeatingSubstring(S, mid):
                high = mid - 1
            else:
                low = mid + 1
        return high

    def hasRepeatingSubstring(self, S, l):
        seen = set()
        N = len(S)
        for i in range(N - l + 1):
            if S[i:i + l] not in seen:
                seen.add(S[i:i + l])
            else:
                return True
        return False
        
# leetcode submit region end(Prohibit modification and deletion)
