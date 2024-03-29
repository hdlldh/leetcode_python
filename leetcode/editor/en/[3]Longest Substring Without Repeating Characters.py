#Given a string, find the length of the longest substring without repeating characters. 
#
# 
# Example 1: 
#
# 
#Input: "abcabcbb"
#Output: 3 
#Explanation: The answer is "abc", with the length of 3. 
# 
#
# 
# Example 2: 
#
# 
#Input: "bbbbb"
#Output: 1
#Explanation: The answer is "b", with the length of 1.
# 
#
# 
# Example 3: 
#
# 
#Input: "pwwkew"
#Output: 3
#Explanation: The answer is "wke", with the length of 3. 
#             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
# 
# 
# 
# 
# Related Topics Hash Table Two Pointers String Sliding Window



#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        hmap = {}
        left  = -1
        ans = 0
        for i, ch in enumerate(s):
            if ch in hmap and hmap[ch]>left:
                left = hmap[ch]
            ans = max(ans, i-left)
            hmap[ch] = i
        return ans
#leetcode submit region end(Prohibit modification and deletion)
