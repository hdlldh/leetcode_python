#Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number. 
#
# The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. 
#
# Note: 
#
# 
# Your returned answers (both index1 and index2) are not zero-based. 
# You may assume that each input would have exactly one solution and you may not use the same element twice. 
# 
#
# Example: 
#
# 
#Input: numbers = [2,7,11,15], target = 9
#Output: [1,2]
#Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2. 
# Related Topics Array Two Pointers Binary Search



#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(numbers)
        i = 0
        j = n-1
        while i<j:
            if numbers[i]+numbers[j]> target:
                j-=1
            elif numbers[i]+numbers[j]<target:
                i+=1
            else:
                return [i+1,j+1]
#leetcode submit region end(Prohibit modification and deletion)
