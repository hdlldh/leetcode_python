#Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram. 
#
# 
#
# 
#Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3]. 
#
# 
#
# 
#The largest rectangle is shown in the shaded area, which has area = 10 unit. 
#
# 
#
# Example: 
#
# 
#Input: [2,1,5,6,2,3]
#Output: 10
# 
# Related Topics Array Stack



#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        heights.append(0)
        stack = []
        ans = 0
        for i, h in enumerate(heights):
            while stack and h<=heights[stack[-1]]:
                cur = stack.pop()
                if stack: ans = max(ans, (i-stack[-1]-1)*heights[cur])
                else: ans = max(ans, i*heights[cur])
            stack.append(i)
        return ans
        
#leetcode submit region end(Prohibit modification and deletion)
