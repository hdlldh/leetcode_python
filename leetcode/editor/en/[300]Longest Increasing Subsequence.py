#Given an unsorted array of integers, find the length of longest increasing subsequence. 
#
# Example: 
#
# 
#Input: [10,9,2,5,3,7,101,18]
#Output: 4 
#Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4. 
#
# Note: 
#
# 
# There may be more than one LIS combination, it is only necessary for you to return the length. 
# Your algorithm should run in O(n2) complexity. 
# 
#
# Follow up: Could you improve it to O(n log n) time complexity? 
# Related Topics Binary Search Dynamic Programming



#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0: return 0
        arr = []
        for num in nums:
            k = len(arr)
            low = 0
            high = len(arr)-1
            while low<=high:
                mid = low + (high-low)//2
                if arr[mid]>=num:
                    high = mid -1
                else:
                    low = mid +1
            if low==k:
                arr.append(num)
            else:
                arr[low] = num
        return len(arr)

        
#leetcode submit region end(Prohibit modification and deletion)
