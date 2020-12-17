#Given an array arr of positive integers, consider all binary trees such that: 
#
# 
# Each node has either 0 or 2 children; 
# The values of arr correspond to the values of each leaf in an in-order traversal of the tree. (Recall that a node is a leaf if and only if it has 0 children.) 
# The value of each non-leaf node is equal to the product of the largest leaf value in its left and right subtree respectively. 
# 
#
# Among all possible binary trees considered, return the smallest possible sum of the values of each non-leaf node. It is guaranteed this sum fits into a 32-bit integer. 
#
# 
# Example 1: 
#
# 
#Input: arr = [6,2,4]
#Output: 32
#Explanation:
#There are two possible trees.  The first has non-leaf node sum 36, and the second has non-leaf node sum 32.
#
#    24            24
#   /  \          /  \
#  12   4        6    8
# /  \               / \
#6    2             2   4
# 
#
# 
# Constraints: 
#
# 
# 2 <= arr.length <= 40 
# 1 <= arr[i] <= 15 
# It is guaranteed that the answer fits into a 32-bit signed integer (ie. it is less than 2^31). 
# Related Topics Dynamic Programming Stack Tree



#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def mctFromLeafValues(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        N = len(arr)
        maxi = [[-float('inf')] * N for _ in range(N)]
        for i in range(N):
            maxi[i][i] = arr[i]
            for j in range(i + 1, N):
                maxi[i][j] = max(maxi[i][j - 1], arr[j])
        mem = {}

        def helper(left, right, mem):
            if left == right: return 0
            if (left, right) in mem: return mem[(left, right)]
            ans = float('inf')

            for i in range(left, right):
                ans = min(ans, maxi[left][i] * maxi[i + 1][right] + helper(left, i, mem) + helper(i + 1, right, mem))

            mem[(left, right)] = ans
            return ans

        helper(0, N - 1, mem)
        return mem[(0, N - 1)]
#leetcode submit region end(Prohibit modification and deletion)
