# Given a positive 32-bit integer n, you need to find the smallest 32-bit intege
# r which has exactly the same digits existing in the integer n and is greater in 
# value than n. If no such positive 32-bit integer exists, you need to return -1. 
# 
# 
#  Example 1: 
# 
#  
# Input: 12
# Output: 21
#  
# 
#  
# 
#  Example 2: 
# 
#  
# Input: 21
# Output: -1
#  
# 
#  
#  Related Topics String


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def nextGreaterElement(self, n):
        """
        :type n: int
        :rtype: int
        """
        arr = []
        while n:
            arr.append(n % 10)
            n = n // 10
        arr.reverse()
        m = len(arr)
        if m == 1: return -1
        left = None
        for i in range(m - 2, -1, -1):
            if arr[i] < arr[i + 1]:
                left = i
                break
        if left is None: return -1

        right = None
        for i in range(m - 1, left, -1):
            if arr[i] > arr[left]:
                right = i
                break
        arr[left], arr[right] = arr[right], arr[left]
        left = left + 1
        right = m - 1
        while left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
        num = 0
        for a in arr: num = 10 * num + a
        if num > 0x7FFFFFFF: return -1
        return num
        
# leetcode submit region end(Prohibit modification and deletion)
