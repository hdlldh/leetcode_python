# Given an array nums, we call (i, j) an important reverse pair if i < j and num
# s[i] > 2*nums[j]. 
# 
#  You need to return the number of important reverse pairs in the given array. 
# 
# 
#  Example1:
#  
# Input: [1,3,2,3,1]
# Output: 2
#  
# 
#  Example2:
#  
# Input: [2,4,3,5,1]
# Output: 3
#  
# 
#  Note: 
#  
#  The length of the given array will not exceed 50,000. 
#  All the numbers in the input array are in the range of 32-bit integer. 
#  
#  Related Topics Binary Search Divide and Conquer Sort Binary Indexed Tree Segm
# ent Tree


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def reversePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n==0: return 0
        tmp = [nums[-1]]
        ans = 0
        for i in range(n-2, -1, -1):
            cur = nums[i]
            low = 0
            high = len(tmp) -1
            while low <= high:
                mid = (low+high)//2
                if 2*tmp[mid] >= cur: high = mid -1
                else: low = mid + 1
            #print(tmp, low, cur)
            ans += low

            low = 0
            high = len(tmp) - 1
            while low <= high:
                mid = (low + high) // 2
                if tmp[mid] >= cur: high = mid -1
                else: low = mid + 1
            tmp.insert(low, cur)
        return ans


    def reversePairs2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return self.merge(nums, 0, len(nums)-1)

    def merge(self, nums, left, right):
        if left >= right: return 0
        mid = (left + right) //2
        res = self.merge(nums, left, mid) + self.merge(nums, mid+1, right)
        j = mid + 1
        #print(res, nums[left:mid+1], nums[mid+1: right+1])
        for i in range(left, mid+1):
            while j<=right and nums[i]>2*nums[j]: j+=1
            res += j - (mid + 1)
        #print(res)
        i = left
        j = mid + 1
        k = left
        tmp = [0] * len(nums)
        while i <= mid and j<=right:
            if nums[i] <= nums[j]:
                tmp[k] = nums[i]
                i += 1
            else:
                tmp[k] = nums[j]
                j += 1
            k += 1
        while i<= mid:
            tmp[k] = nums[i]
            i += 1
            k += 1
        while j <= right:
            tmp[k] = nums[j]
            j += 1
            k += 1
        for k in range(left, right + 1):
            nums[k] = tmp[k]
        return res
        
# leetcode submit region end(Prohibit modification and deletion)
