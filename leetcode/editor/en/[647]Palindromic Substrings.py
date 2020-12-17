#Given a string, your task is to count how many palindromic substrings in this s
#tring. 
#
# The substrings with different start indexes or end indexes are counted as diff
#erent substrings even they consist of same characters. 
#
# Example 1: 
#
# 
#Input: "abc"
#Output: 3
#Explanation: Three palindromic strings: "a", "b", "c".
# 
#
# 
#
# Example 2: 
#
# 
#Input: "aaa"
#Output: 6
#Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
# 
#
# 
#
# Note: 
#
# 
# The input string length won't exceed 1000. 
# 
#
# Related Topics String Dynamic Programming




#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        ans = 0
        for i in range(n):
            l = i
            r = i
            count = 0
            while l>=0 and r<n and s[l]==s[r]:
                count+=1
                l-=1
                r+=1
            ans += count
        for i in range(1, n):
            l=i-1
            r=i
            count = 0
            while l>=0 and r<n and s[l]==s[r]:
                count+=1
                l-=1
                r+=1
            ans += count
        return ans
        
#leetcode submit region end(Prohibit modification and deletion)
