#Given an array which consists of non-negative integers and an integer m, you can split the array into m non-empty continuous subarrays. Write an algorithm to minimize the largest sum among these m subarrays.
# 
#
# Note: 
#If n is the length of array, assume the following constraints are satisfied:
# 
# 1 ≤ n ≤ 1000 
# 1 ≤ m ≤ min(50, n) 
# 
# 
#
# Examples: 
# 
#Input:
#nums = [7,2,5,10,8]
#m = 2
#
#Output:
#18
#
#Explanation:
#There are four ways to split nums into two subarrays.
#The best way is to split it into [7,2,5] and [10,8],
#where the largest sum among the two subarrays is only 18.
# 
# Related Topics Binary Search Dynamic Programming



#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        n = len(nums)
        psum = [0] * (n+1)
        dp = [[float('inf')] * (n + 1) for _ in range(m + 1)]
        for i in range(1, n+1):
            psum[i] = psum[i-1]+nums[i-1]
            dp[1][i] = psum[i]
        for k in range(2, m+1):
            for i in range(1, n+1):
                for j in range(i):
                    dp[k][i] = min(dp[k][i], max(dp[k-1][j], psum[i]-psum[j]))
        return dp[m][n]
        
#leetcode submit region end(Prohibit modification and deletion)
