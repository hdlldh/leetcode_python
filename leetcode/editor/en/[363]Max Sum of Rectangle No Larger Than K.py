#Given a non-empty 2D matrix matrix and an integer k, find the max sum of a rectangle in the matrix such that its sum is no larger than k. 
#
# Example: 
#
# 
#Input: matrix = [[1,0,1],[0,-2,3]], k = 2
#Output: 2 
#Explanation: Because the sum of rectangle [[0, 1], [-2, 3]] is 2,
#             and 2 is the max number no larger than k (k = 2). 
#
# Note: 
#
# 
# The rectangle inside the matrix must have an area > 0. 
# What if the number of rows is much larger than the number of columns? 
# Related Topics Binary Search Dynamic Programming Queue



#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def maxSumSubmatrix(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        m, n = len(matrix), len(matrix[0])
        rowLarger = True if m > n else False
        if rowLarger:
            m, n = n, m
        ans = -float('inf')
        for i in range(m):
            array = [0] * n
            for j in range(i, -1, -1):
                for l in range(n):
                    if not rowLarger:
                        array[l] += matrix[j][l]
                    else:
                        array[l] += matrix[l][j]
                ans = max(ans, self.maxSumSubarray(array, k))
        return ans

    def maxSumSubarray(self, array, k):
        sorted_sum = [0]
        ans = -float('inf')
        acc_sum = 0
        for num in array:
            acc_sum += num
            low = 0
            high = len(sorted_sum) - 1
            while low <= high:
                mid = low + (high - low) // 2
                if acc_sum - sorted_sum[mid] <= k:
                    high = mid - 1
                else:
                    low = mid + 1
            if low != len(sorted_sum):
                ans = max(ans, acc_sum - sorted_sum[low])
            low = 0
            high = len(sorted_sum) - 1
            while low <= high:
                mid = low + (high - low) // 2
                if acc_sum <= sorted_sum[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            sorted_sum.insert(low, acc_sum)
        return ans

#leetcode submit region end(Prohibit modification and deletion)
