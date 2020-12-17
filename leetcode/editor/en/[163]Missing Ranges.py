#Given a sorted integer array nums, where the range of elements are in the inclusive range [lower, upper], return its missing ranges. 
#
# Example: 
#
# 
#Input: nums = [0, 1, 3, 50, 75], lower = 0 and upper = 99,
#Output: ["2", "4->49", "51->74", "76->99"]
# 
# Related Topics Array



#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        n = len(nums)
        ans = []
        if n == 0: return [self.getRanges(lower, upper)]
        if nums[0] != lower: ans.append(self.getRanges(lower, nums[0] - 1))
        i = 1
        while i<n:
            if nums[i] > nums[i-1]+1:
                ans.append(self.getRanges(nums[i-1] + 1, nums[i] - 1))
            i += 1
        if nums[-1] != upper: ans.append(self.getRanges(nums[-1] + 1, upper))
        return ans

    def getRanges(self, start, end):
        s = str(start)
        if start!=end:
            e = str(end)
            return s+'->'+e
        return s
        
#leetcode submit region end(Prohibit modification and deletion)
