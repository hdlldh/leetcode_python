#
#Given an unsorted array of integers, find the number of longest increasing subsequence.
# 
#
# Example 1: 
# 
#Input: [1,3,5,4,7]
#Output: 2
#Explanation: The two longest increasing subsequence are [1, 3, 4, 7] and [1, 3, 5, 7].
# 
# 
#
# Example 2: 
# 
#Input: [2,2,2,2,2]
#Output: 5
#Explanation: The length of longest continuous increasing subsequence is 1, and there are 5 subsequences' length is 1, so output 5.
# 
# 
#
# Note:
#Length of the given array will be not exceed 2000 and the answer is guaranteed to be fit in 32-bit signed int.
# Related Topics Dynamic Programming



#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def findNumberOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        length = [1] * n # number of longest increasing subseq ending at i
        count = [1] * n  # count of longest increasing subseq ending at i
        maxLen = 1
        for i in range(1, n):
            for j in range(i):
                if nums[i]<= nums[j]: continue
                if length[i] == length[j] + 1: count[i] += count[j]
                elif length[i] < length[j] + 1:
                    count[i] = count[j]
                    length[i] = length[j] + 1
            maxLen = max(maxLen, length[i])

        ans = 0
        for i in range(n):
            if length[i]==maxLen: ans+=count[i]
        return ans
        
#leetcode submit region end(Prohibit modification and deletion)
