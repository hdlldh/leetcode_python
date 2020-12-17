#Given a positive integer n, generate a square matrix filled with elements from 1 to n2 in spiral order. 
#
# Example: 
#
# 
#Input: 3
#Output:
#[
# [ 1, 2, 3 ],
# [ 8, 9, 4 ],
# [ 7, 6, 5 ]
#]
# 
# Related Topics Array



#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        left, right = 0, n-1
        top, bottom = 0, n-1
        ans = [[0]*n for _ in range(n)]
        num = 1
        while True:
            for j in range(left, right+1):
                ans[top][j] = num
                num += 1
            top += 1
            if top>bottom: break
            for i in range(top, bottom+1):
                ans[i][right] = num
                num += 1
            right -= 1
            if left>right: break
            for j in range(right, left-1, -1):
                ans[bottom][j] = num
                num += 1
            bottom -= 1
            if top>bottom: break
            for i in range(bottom, top-1, -1):
                ans[i][left] = num
                num += 1
            left += 1
            if left>right: break
        return ans
        
#leetcode submit region end(Prohibit modification and deletion)
