# Given a string s and a non-empty string p, find all the start indices of p's a
# nagrams in s. 
# 
#  Strings consists of lowercase English letters only and the length of both str
# ings s and p will not be larger than 20,100. 
# 
#  The order of output does not matter. 
# 
#  Example 1:
#  
# Input:
# s: "cbaebabacd" p: "abc"
# 
# Output:
# [0, 6]
# 
# Explanation:
# The substring with start index = 0 is "cba", which is an anagram of "abc".
# The substring with start index = 6 is "bac", which is an anagram of "abc".
#  
#  
# 
#  Example 2:
#  
# Input:
# s: "abab" p: "ab"
# 
# Output:
# [0, 1, 2]
# 
# Explanation:
# The substring with start index = 0 is "ab", which is an anagram of "ab".
# The substring with start index = 1 is "ba", which is an anagram of "ab".
# The substring with start index = 2 is "ab", which is an anagram of "ab".
#  
#  Related Topics Hash Table


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        m, n = len(s), len(p)
        ans = []
        if n > m: return ans
        counter_p = collections.Counter(p)
        for i in range(m - n + 1):
            if i == 0:
                counter_s = collections.Counter(s[:n])
            else:
                counter_s[s[i - 1]] -= 1
                if counter_s[s[i - 1]] == 0: del counter_s[s[i - 1]]
                counter_s[s[i + n - 1]] += 1
            if counter_p == counter_s:
                ans.append(i)

        return ans
        
# leetcode submit region end(Prohibit modification and deletion)
