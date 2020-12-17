# 
# Given a non-negative integer, you could swap two digits at most once to get th
# e maximum valued number. Return the maximum valued number you could get.
#  
# 
#  Example 1: 
#  
# Input: 2736
# Output: 7236
# Explanation: Swap the number 2 and the number 7.
#  
#  
# 
#  Example 2: 
#  
# Input: 9973
# Output: 9973
# Explanation: No swap.
#  
#  
# 
# 
#  Note: 
#  
#  The given number is in the range [0, 108] 
#  
#  Related Topics Array Math


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        nums = [int(ch) for ch in str(num)]
        n = len(nums)
        if n==1: return num
        right = [n-1] * n
        for i in range(n-2, -1, -1):
            if nums[i] > nums[right[i+1]]:
                right[i] = i
            else:
                right[i] = right[i+1]

        for i in range(n-1):
            if nums[i] < nums[right[i+1]]:
                nums[i], nums[right[i+1]] = nums[right[i+1]], nums[i]
                break
        ans = 0
        for num in nums: ans = ans*10+num
        return ans




# leetcode submit region end(Prohibit modification and deletion)
