#In a town, there are N people labelled from 1 to N. There is a rumor that one o
#f these people is secretly the town judge. 
#
# If the town judge exists, then: 
#
# 
# The town judge trusts nobody. 
# Everybody (except for the town judge) trusts the town judge. 
# There is exactly one person that satisfies properties 1 and 2. 
# 
#
# You are given trust, an array of pairs trust[i] = [a, b] representing that the
# person labelled a trusts the person labelled b. 
#
# If the town judge exists and can be identified, return the label of the town j
#udge. Otherwise, return -1. 
#
# 
#
# Example 1: 
#
# 
#Input: N = 2, trust = [[1,2]]
#Output: 2
# 
#
# 
# Example 2: 
#
# 
#Input: N = 3, trust = [[1,3],[2,3]]
#Output: 3
# 
#
# 
# Example 3: 
#
# 
#Input: N = 3, trust = [[1,3],[2,3],[3,1]]
#Output: -1
# 
#
# 
# Example 4: 
#
# 
#Input: N = 3, trust = [[1,2],[2,3]]
#Output: -1
# 
#
# 
# Example 5: 
#
# 
#Input: N = 4, trust = [[1,3],[1,4],[2,3],[2,4],[4,3]]
#Output: 3 
#
# 
# 
# 
# 
# 
#
# Note: 
#
# 
# 1 <= N <= 1000 
# trust.length <= 10000 
# trust[i] are all different 
# trust[i][0] != trust[i][1] 
# 1 <= trust[i][0], trust[i][1] <= N 
# 
# Related Topics Graph




#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def findJudge(self, N, trust):
        """
        :type N: int
        :type trust: List[List[int]]
        :rtype: int
        """
        candidates = [1] * N
        for a, b in trust:
            candidates[a - 1] = 0
            candidates[b - 1] += 1
        for i in range(N):
            if candidates[i] == N: return i + 1
        return -1
#leetcode submit region end(Prohibit modification and deletion)
