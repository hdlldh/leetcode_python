#You are given an integer array nums and you have to return a new counts array. The counts array has the property where counts[i] is the number of smaller elements to the right of nums[i]. 
#
# Example: 
#
# 
#Input: [5,2,6,1]
#Output: [2,1,1,0] 
#Explanation:
#To the right of 5 there are 2 smaller elements (2 and 1).
#To the right of 2 there is only 1 smaller element (1).
#To the right of 6 there is 1 smaller element (1).
#To the right of 1 there is 0 smaller element.
# Related Topics Binary Search Divide and Conquer Sort Binary Indexed Tree Segment Tree



#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        if n==0: return []
        ans = [0]
        if n==1: return ans
        arr = [nums[-1]]
        for i in range(n-2, -1, -1):
            num = nums[i]
            k = len(arr)
            low = 0
            high = k-1
            while low<=high:
                mid = low + (high-low)//2
                if arr[mid]>=num: high = mid -1
                else: low = mid+1
            arr.insert(low, num)
            ans.append(low)
        ans.reverse()
        return ans


#leetcode submit region end(Prohibit modification and deletion)
