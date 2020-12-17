#Given a string, find the length of the longest substring T that contains at most k distinct characters. 
#
# Example 1: 
#
# 
# 
#Input: s = "eceba", k = 2
#Output: 3
#Explanation: T is "ece" which its length is 3. 
#
# 
# Example 2: 
#
# 
#Input: s = "aa", k = 1
#Output: 2
#Explanation: T is "aa" which its length is 2.
# 
# 
# Related Topics Hash Table String Sliding Window



#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        n = len(s)
        hmap = {}
        i = 0
        j = 0
        ans = 0
        while j<n:
            hmap[s[j]] = hmap.get(s[j], 0)+1
            j += 1
            while len(hmap)>k:
                hmap[s[i]] -= 1
                if hmap[s[i]] == 0: del hmap[s[i]]
                i +=1
            ans = max(ans, j-i)
        return ans

        
#leetcode submit region end(Prohibit modification and deletion)
