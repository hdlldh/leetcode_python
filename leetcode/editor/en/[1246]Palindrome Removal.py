# Given an integer array arr, in one move you can select a palindromic subarray 
# arr[i], arr[i+1], ..., arr[j] where i <= j, and remove that subarray from the gi
# ven array. Note that after removing a subarray, the elements on the left and on 
# the right of that subarray move to fill the gap left by the removal. 
# 
#  Return the minimum number of moves needed to remove all numbers from the arra
# y. 
# 
#  
#  Example 1: 
# 
#  
# Input: arr = [1,2]
# Output: 2
#  
# 
#  Example 2: 
# 
#  
# Input: arr = [1,3,4,1,5]
# Output: 3
# Explanation: Remove [4] then remove [1,3,1] then remove [5].
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= arr.length <= 100 
#  1 <= arr[i] <= 20 
#  
#  Related Topics Dynamic Programming


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def minimumMoves(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        N = len(arr)
        dp = [[0] * N for _ in range(N)]

        for l in range(1, N + 1):
            for i in range(N - l + 1):
                j = i + l - 1
                if l == 1:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i][j - 1] + 1
                    if arr[j] == arr[j - 1]:
                        dp[i][j] = min(dp[i][j], dp[i][j - 2] + 1)
                    for k in range(i, j - 1):
                        if arr[j] == arr[k]:
                            if k > 0:
                                dp[i][j] = min(dp[i][j], dp[i][k - 1] + dp[k + 1][j - 1])
                            else:
                                dp[i][j] = min(dp[i][j], dp[k + 1][j - 1])
            # print(dp)
        return dp[0][N - 1]
        
# leetcode submit region end(Prohibit modification and deletion)
