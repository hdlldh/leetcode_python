# Given three integer arrays arr1, arr2 and arr3 sorted in strictly increasing o
# rder, return a sorted array of only the integers that appeared in all three arra
# ys. 
# 
#  
#  Example 1: 
# 
#  
# Input: arr1 = [1,2,3,4,5], arr2 = [1,2,5,7,9], arr3 = [1,3,4,5,8]
# Output: [1,5]
# Explanation: Only 1 and 5 appeared in the three arrays.
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= arr1.length, arr2.length, arr3.length <= 1000 
#  1 <= arr1[i], arr2[i], arr3[i] <= 2000 
#  
#  Related Topics Hash Table Two Pointers


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def arraysIntersection(self, arr1, arr2, arr3):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :type arr3: List[int]
        :rtype: List[int]
        """
        ans = []
        i = 0
        j = 0
        k = 0
        m = len(arr1)
        n = len(arr2)
        l = len(arr3)
        while i<m and j<n and k<l:
            if arr1[i]==arr2[j]==arr3[k]:
                ans.append(arr1[i])
                i+=1
                j+=1
                k+=1
            else:
                mx = min(arr1[i], arr2[j], arr3[k])
                if arr1[i] == mx: i+=1
                if arr2[j] == mx: j+=1
                if arr3[k] == mx: k+=1
        return ans
        
# leetcode submit region end(Prohibit modification and deletion)
