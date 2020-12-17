#Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area. 
#
# Example: 
#
# 
#Input:
#[
#  ["1","0","1","0","0"],
#  ["1","0","1","1","1"],
#  ["1","1","1","1","1"],
#  ["1","0","0","1","0"]
#]
#Output: 6
# 
# Related Topics Array Hash Table Dynamic Programming Stack



#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        m = len(matrix)
        if m == 0: return 0
        n = len(matrix[0])
        ans = 0
        heights = [0] * (n + 1)
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '0':
                    heights[j] = 0
                else:
                    heights[j] += 1
            ans = max(ans, self.largestRectangleArea(heights))
        return ans

    def largestRectangleArea(self, heights):
        ans = 0
        stack = []
        for i, h in enumerate(heights):
            while stack and h <= heights[stack[-1]]:
                cur = stack.pop()
                if stack:
                    ans = max(ans, (i - stack[-1] - 1) * heights[cur])
                else:
                    ans = max(ans, i * heights[cur])
            stack.append(i)
        return ans
#leetcode submit region end(Prohibit modification and deletion)
