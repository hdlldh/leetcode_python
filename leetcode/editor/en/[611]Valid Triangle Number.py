#Given an array consists of non-negative integers, your task is to count the num
#ber of triplets chosen from the array that can make triangles if we take them as
# side lengths of a triangle.
#
# Example 1: 
# 
#Input: [2,2,3,4]
#Output: 3
#Explanation:
#Valid combinations are: 
#2,3,4 (using the first 2)
#2,3,4 (using the second 2)
#2,2,3
# 
# 
#
# Note: 
# 
# The length of the given array won't exceed 1000. 
# The integers in the given array are in the range of [0, 1000]. 
# 
# 
# Related Topics Array




#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        n = len(nums)
        nums.sort()
        if n<3: return ans
        for a in range(n-2):
            if nums[a]==0: continue
            c = a+2
            for b in range(a+1, n-1):
                while (c<n and nums[c]-nums[b]<nums[a]): c+=1
                ans += c-b-1
        return ans

#leetcode submit region end(Prohibit modification and deletion)
