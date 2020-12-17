#Given a string s, partition s such that every substring of the partition is a palindrome. 
#
# Return all possible palindrome partitioning of s. 
#
# Example: 
#
# 
#Input: "aab"
#Output:
#[
#  ["aa","b"],
#  ["a","a","b"]
#]
# 
# Related Topics Backtracking



#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        mem = self.findPalindrome(s)
        print(mem)
        ans = []
        self.dfs(s, 0, mem, [], ans)
        return ans

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

    def dfs(self, s, start, mem, out, ans):
        if (start==len(s)):
            ans.append(out[:])
            return
        for i in range(start, len(s)):
            if mem[start][i]:
                out.append(s[start:i+1])
                self.dfs(s, i+1, mem, out, ans)
                out.pop()
#leetcode submit region end(Prohibit modification and deletion)
