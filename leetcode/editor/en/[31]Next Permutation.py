#Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers. 
#
# If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order). 
#
# The replacement must be in-place and use only constant extra memory. 
#
# Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column. 
#
# 1,2,3 → 1,3,2 
#3,2,1 → 1,2,3 
#1,1,5 → 1,5,1 
# Related Topics Array



#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i = n-1
        left = -1

        for i in range(n-1, 0, -1):
            if nums[i-1] < nums[i]:
                left = i-1
                break

        if left == -1:
            nums.sort()
            return

        for i in range(n-1, left, -1):
            if nums[i] > nums[left]:
                right = i
                break

        nums[left], nums[right] = nums[right], nums[left]
        i = left +1
        j = n-1
        while i<j:
            nums[i], nums[j] = nums[j], nums[i]
            i+=1
            j-=1



        
#leetcode submit region end(Prohibit modification and deletion)
