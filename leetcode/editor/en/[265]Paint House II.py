#There are a row of n houses, each house can be painted with one of the k colors. The cost of painting each house with a certain color is different. You have to paint all the houses such that no two adjacent houses have the same color. 
#
# The cost of painting each house with a certain color is represented by a n x k cost matrix. For example, costs[0][0] is the cost of painting house 0 with color 0; costs[1][2] is the cost of painting house 1 with color 2, and so on... Find the minimum cost to paint all houses. 
#
# Note: 
#All costs are positive integers. 
#
# Example: 
#
# 
#Input: [[1,5,3],[2,9,4]]
#Output: 5
#Explanation: Paint house 0 into color 0, paint house 1 into color 2. Minimum cost: 1 + 4 = 5; 
#             Or paint house 0 into color 2, paint house 1 into color 0. Minimum cost: 3 + 2 = 5. 
# 
#
# Follow up: 
#Could you solve it in O(nk) runtime? 
# Related Topics Dynamic Programming



#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def minCostII(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        n = len(costs)
        if n==0: return 0
        k = len(costs[0])
        last0, last1 = 0, 0
        curr0, curr1 = None, None
        dp = [[0]*k for _ in range(n+1)]

        for i in range(1, n+1):
            min0, min1 = float('inf'), float('inf')
            for j in range(k):
                if j!=last0:
                    dp[i][j] = dp[i-1][last0] + costs[i-1][j]
                else:
                    dp[i][j] = dp[i-1][last1] + costs[i-1][j]
                if dp[i][j]< min0:
                    min0, min1 = dp[i][j], min0
                    curr0, curr1 = j, curr0
                elif dp[i][j]<min1:
                    min1 = dp[i][j]
                    curr1 = j
            last0, last1 = curr0, curr1
        return dp[n][curr0]

#leetcode submit region end(Prohibit modification and deletion)
