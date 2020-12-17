#
#Find the length of the longest substring T of a given string (consists of lowercase letters only) such that every character in T appears no less than k times.
# 
#
# Example 1:
# 
#Input:
#s = "aaabb", k = 3
#
#Output:
#3
#
#The longest substring is "aaa", as 'a' is repeated 3 times.
# 
# 
#
# Example 2:
# 
#Input:
#s = "ababbc", k = 2
#
#Output:
#5
#
#The longest substring is "ababb", as 'a' is repeated 2 times and 'b' is repeated 3 times.
# 
#



#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        n = len(s)
        counter = collections.Counter(s)
        ans = 0
        splitSet=set()
        for ch in counter:
            if counter[ch] < k: splitSet.add(ch)

        if not splitSet: return n
        i = 0
        j = 0
        while (j<n):
            if s[j] in splitSet:
                if j>i:
                    ans = max(ans, self.longestSubstring(s[i:j], k))
                i = j+1
            j+=1
        if i!=j: ans = max(ans, self.longestSubstring(s[i:j], k))
        return ans



#leetcode submit region end(Prohibit modification and deletion)
