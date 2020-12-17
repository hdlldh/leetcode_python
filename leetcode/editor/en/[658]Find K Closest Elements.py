# 
# Given a sorted array, two integers k and x, find the k closest elements to x i
# n the array. The result should also be sorted in ascending order.
# If there is a tie, the smaller elements are always preferred.
#  
# 
#  Example 1: 
#  
# Input: [1,2,3,4,5], k=4, x=3
# Output: [1,2,3,4]
#  
#  
# 
# 
#  Example 2: 
#  
# Input: [1,2,3,4,5], k=4, x=-1
# Output: [1,2,3,4]
#  
#  
# 
#  Note: 
#  
#  The value k is positive and will always be smaller than the length of the sor
# ted array. 
#  Length of the given array is positive and will not exceed 104 
#  Absolute value of elements in the array and x will not exceed 104 
#  
#  
# 
#  
# 
#  
# UPDATE (2017/9/19): 
# The arr parameter had been changed to an array of integers (instead of a list 
# of integers). Please reload the code definition to get the latest changes.
#  Related Topics Binary Search


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        low = 0
        high = len(arr) -k -1
        while low <= high:
            mid = (low + high) //2
            if x - arr[mid] > arr[mid+k] -x:
                low = mid + 1
            else:
                high = mid -1
        return arr[low:low+k]

    def findClosestElements2(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        if x <= arr[0]: return arr[:k]
        elif x>=arr[-1]: return arr[-k:]

        n = len(arr)
        low = 0
        high = n - 1
        ans = []
        while low <=high:
            mid = low + (high-low)//2
            if arr[mid]>= x: high = mid -1
            else: low = mid + 1

        if x -arr[high] <= arr[low] -x:
            mid = high
        else:
            mid = low
        ans.append(arr[mid])
        k = k-1
        left = mid -1
        right = mid + 1
        while k>0:
            if left >=0 and right < n:
                if abs(arr[left]-x) <= abs(arr[right]-x):
                    ans.insert(0, arr[left])
                    left -= 1
                else:
                    ans.append(arr[right])
                    right += 1
            elif left >=0:
                ans.insert(0, arr[left])
                left -= 1
            elif right <n:
                ans.append(arr[right])
                right += 1
            k -= 1
        return ans


        
# leetcode submit region end(Prohibit modification and deletion)
