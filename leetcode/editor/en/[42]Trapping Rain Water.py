#Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining. 
#
# 
#The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image! 
#
# Example: 
#
# 
#Input: [0,1,0,2,1,0,1,3,2,1,2,1]
#Output: 6 
# Related Topics Array Two Pointers Stack



#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        l2r = [0] * n
        r2l = [0] * n
        for i in range(1,n):
            l2r[i] = max(l2r[i-1],height[i-1])

        for i in range(n-2, 0, -1):
            r2l[i] = max(r2l[i+1],height[i+1])

        ans = 0
        for i in range(1,n-1):
            ans += max(0, min(l2r[i], r2l[i]) - height[i])
        return ans
        
#leetcode submit region end(Prohibit modification and deletion)
