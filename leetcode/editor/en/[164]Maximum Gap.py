#Given an unsorted array, find the maximum difference between the successive elements in its sorted form. 
#
# Return 0 if the array contains less than 2 elements. 
#
# Example 1: 
#
# 
#Input: [3,6,9,1]
#Output: 3
#Explanation: The sorted form of the array is [1,3,6,9], either
#             (3,6) or (6,9) has the maximum difference 3. 
#
# Example 2: 
#
# 
#Input: [10]
#Output: 0
#Explanation: The array contains less than 2 elements, therefore return 0. 
#
# Note: 
#
# 
# You may assume all elements in the array are non-negative integers and fit in the 32-bit signed integer range. 
# Try to solve it in linear time/space. 
# 
# Related Topics Sort



#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n<=1: return 0
        maxVal = max(nums)
        minVal = min(nums)
        bkSize = (maxVal-minVal)//n +1
        bkNum = (maxVal-minVal)//bkSize +1
        bkMax = [-float('inf')]*bkNum
        bkMin = [float('inf')]*bkNum
        visited = set()
        ans = -float('inf')
        for i in range(n):
            bkId = (nums[i]-minVal)//bkSize
            bkMax[bkId] = max(bkMax[bkId], nums[i])
            bkMin[bkId] = min(bkMin[bkId], nums[i])
            visited.add(bkId)
        pre = minVal
        for i in range(bkNum):
            if i not in visited: continue
            ans = max(ans, bkMin[i] - pre)
            pre = bkMax[i]
        return ans

#leetcode submit region end(Prohibit modification and deletion)
