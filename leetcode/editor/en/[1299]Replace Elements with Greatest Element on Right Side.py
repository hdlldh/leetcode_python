# Given an array arr, replace every element in that array with the greatest elem
# ent among the elements to its right, and replace the last element with -1. 
# 
#  After doing so, return the array. 
# 
#  
#  Example 1: 
#  Input: arr = [17,18,5,4,6,1]
# Output: [18,6,6,6,1,-1]
#  
#  
#  Constraints: 
# 
#  
#  1 <= arr.length <= 10^4 
#  1 <= arr[i] <= 10^5 
#  Related Topics Array


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        n = len(arr)
        ans = [-1] * n
        if n== 1: return ans
        maxi = arr[-1]
        for i in range(n-2, -1, -1):
            ans[i] = maxi
            maxi = max(maxi, arr[i])
        return ans
        
# leetcode submit region end(Prohibit modification and deletion)
