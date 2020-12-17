#Numbers can be regarded as product of its factors. For example, 
#
# 
#8 = 2 x 2 x 2;
#  = 2 x 4.
# 
#
# Write a function that takes an integer n and return all possible combinations of its factors. 
#
# Note: 
#
# 
# You may assume that n is always positive. 
# Factors should be greater than 1 and less than n. 
# 
#
# Example 1: 
#
# 
#Input: 1
#Output: []
# 
#
# Example 2: 
#
# 
#Input: 37
#Output:[] 
#
# Example 3: 
#
# 
#Input: 12
#Output:
#[
#  [2, 6],
#  [2, 2, 3],
#  [3, 4]
#] 
#
# Example 4: 
#
# 
#Input: 32
#Output:
#[
#  [2, 16],
#  [2, 2, 8],
#  [2, 2, 2, 4],
#  [2, 2, 2, 2, 2],
#  [2, 4, 4],
#  [4, 8]
#]
# 
# Related Topics Backtracking



#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def getFactors(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        ans = []
        self.dfs(n, 2, [], ans)
        return ans

    def dfs(self, n, start, out, ans):
        i = start
        while i*i<=n:
            if n%i==0:
                out.append(i)
                out.append(n//i)
                ans.append(out[:])
                out.pop()
                self.dfs(n//i, i, out, ans)
                out.pop()
            i+=1
        
#leetcode submit region end(Prohibit modification and deletion)
