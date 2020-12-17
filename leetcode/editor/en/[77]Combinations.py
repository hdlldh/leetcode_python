#Given two integers n and k, return all possible combinations of k numbers out of 1 ... n. 
#
# Example: 
#
# 
#Input: n = 4, k = 2
#Output:
#[
#  [2,4],
#  [3,4],
#  [2,3],
#  [1,2],
#  [1,3],
#  [1,4],
#]
# 
# Related Topics Backtracking



#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        ans = []
        self.dfs(n, k, 1, [], ans)
        return ans

    def dfs(self, n, k, start, out, ans):
        if len(out)==k:
            ans.append(out[:])
            return
        for i in range(start, n+1):
            out.append(i)
            self.dfs(n, k, i+1, out, ans)
            out.pop()
#leetcode submit region end(Prohibit modification and deletion)
