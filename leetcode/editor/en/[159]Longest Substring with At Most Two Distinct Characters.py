#Given a string s , find the length of the longest substring t that contains at most 2 distinct characters. 
#
# Example 1: 
#
# 
#Input: "eceba"
#Output: 3
#Explanation: t is "ece" which its length is 3.
# 
#
# Example 2: 
#
# 
#Input: "ccaabbb"
#Output: 5
#Explanation: t is "aabbb" which its length is 5.
# 
# Related Topics Hash Table Two Pointers String Sliding Window



#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """

        hmap = {}
        ans = 0
        j = 0
        for i, ch in enumerate(s):
            if ch not in hmap: hmap[ch] = 1
            else: hmap[ch]+=1
            while len(hmap)>2:
                hmap[s[j]] -= 1
                if hmap[s[j]]==0: del hmap[s[j]]
                j+=1
            ans = max(ans, i-j+1)
        return ans


        
#leetcode submit region end(Prohibit modification and deletion)
