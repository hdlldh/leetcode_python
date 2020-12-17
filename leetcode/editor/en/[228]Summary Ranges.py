#Given a sorted integer array without duplicates, return the summary of its ranges. 
#
# Example 1: 
#
# 
#Input:  [0,1,2,4,5,7]
#Output: ["0->2","4->5","7"]
#Explanation: 0,1,2 form a continuous range; 4,5 form a continuous range.
# 
#
# Example 2: 
#
# 
#Input:  [0,2,3,4,6,8,9]
#Output: ["0","2->4","6","8->9"]
#Explanation: 2,3,4 form a continuous range; 8,9 form a continuous range.
# 
# Related Topics Array



#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        n = len(nums)
        ans = []
        if n==0: return ans
        i = 0
        j = 1
        def summarize(i, j):
            start = str(nums[i])
            if i != j:
                end = str(nums[j])
                return start + '->' + end
            return start


        while j<n:
            if nums[j]!=nums[j-1]+1:
                ans.append(summarize(i, j-1))
                i = j
            j += 1

        ans.append(summarize(i,n-1))
        return ans


#leetcode submit region end(Prohibit modification and deletion)
