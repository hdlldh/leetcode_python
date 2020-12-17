#Given two sparse matrices A and B, return the result of AB. 
#
# You may assume that A's column number is equal to B's row number. 
#
# Example: 
#
# 
#Input:
#
#A = [
#  [ 1, 0, 0],
#  [-1, 0, 3]
#]
#
#B = [
#  [ 7, 0, 0 ],
#  [ 0, 0, 0 ],
#  [ 0, 0, 1 ]
#]
#
#Output:
#
#     |  1 0 0 |   | 7 0 0 |   |  7 0 0 |
#AB = | -1 0 3 | x | 0 0 0 | = | -7 0 3 |
#                  | 0 0 1 |
# 
# Related Topics Hash Table



#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def multiply(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        m = len(A)
        k = len(A[0])
        n = len(B[0])
        ans = [[0]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                for l in range(k):
                    if A[i][l]!=0 and B[l][j]!=0:
                        ans[i][j] += A[i][l]*B[l][j]
        return ans
#leetcode submit region end(Prohibit modification and deletion)
