#Given a string s, partition s such that every substring of the partition is a palindrome. 
#
# Return the minimum cuts needed for a palindrome partitioning of s. 
#
# Example: 
#
# 
#Input: "aab"
#Output: 1
#Explanation: The palindrome partitioning ["aa","b"] could be produced using 1 cut.
# 
# Related Topics Dynamic Programming



#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        mem = self.findPalindrome(s)
        n = len(s)
        dp = [float('inf')]*n
        dp[0] =1
        for i in range(1,n):
            if mem[0][i]:
                dp[i] = 1
                continue
            for j in range(i):
                if mem[j+1][i]:
                    dp[i] = min(dp[i], dp[j]+1)
        return dp[-1]-1

    def findPalindrome(self, s):
        n = len(s)
        ans = [[False] *n for _ in range(n)]
        for i in range(n):
            left = i
            right = i
            while left>=0 and right<n:
                if s[left] ==s[right]:
                    ans[left][right] = True
                else: break
                left-=1
                right+=1
        for i in range(1,n):
            left = i-1
            right = i
            while left>=0 and right<n:
                if s[left] ==s[right]:
                    ans[left][right] = True
                else: break
                left -= 1
                right+=1
        return ans
#leetcode submit region end(Prohibit modification and deletion)
