#There are two sorted arrays nums1 and nums2 of size m and n respectively. 
#
# Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)). 
#
# You may assume nums1 and nums2 cannot be both empty. 
#
# Example 1: 
#
# 
#nums1 = [1, 3]
#nums2 = [2]
#
#The median is 2.0
# 
#
# Example 2: 
#
# 
#nums1 = [1, 2]
#nums2 = [3, 4]
#
#The median is (2 + 3)/2 = 2.5
# 
# Related Topics Array Binary Search Divide and Conquer



#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m = len(nums1)
        n = len(nums2)
        if m>n:
            nums1, nums2 = nums2, nums1
            m, n = n, m

        low = 0
        high = m
        while low<=high:
            mid = low + (high-low)//2
            mid2 = (m+n)//2 - mid
            leftMax1 = nums1[mid-1] if mid>=1 else -float('inf')
            leftMax2 = nums2[mid2-1] if mid2>=1 else -float('inf')
            rightMin1 = nums1[mid] if mid<m else float('inf')
            rightMin2 = nums2[mid2] if mid2<n else float('inf')
            if leftMax1 > rightMin2:
                high = mid - 1
            elif leftMax2 > rightMin1:
                low = mid + 1
            else:
                break
        if (m+n)%2==0:
            return (max(leftMax1,leftMax2) + min(rightMin1,rightMin2))*0.5
        else:
            return min(rightMin1,rightMin2)*1.0

#leetcode submit region end(Prohibit modification and deletion)
