# Given an array A of positive integers (not necessarily distinct), return the l
# exicographically largest permutation that is smaller than A, that can be made wi
# th one swap (A swap exchanges the positions of two numbers A[i] and A[j]). If it
#  cannot be done, then return the same array. 
# 
#  
# 
#  Example 1: 
# 
#  
# Input: [3,2,1]
# Output: [3,1,2]
# Explanation: Swapping 2 and 1.
#  
# 
#  Example 2: 
# 
#  
# Input: [1,1,5]
# Output: [1,1,5]
# Explanation: This is already the smallest permutation.
#  
# 
#  Example 3: 
# 
#  
# Input: [1,9,4,6,7]
# Output: [1,7,4,6,9]
# Explanation: Swapping 9 and 7.
#  
# 
#  Example 4: 
# 
#  
# Input: [3,1,1,3]
# Output: [1,3,1,3]
# Explanation: Swapping 1 and 3.
#  
# 
#  
# 
#  Note: 
# 
#  
#  1 <= A.length <= 10000 
#  1 <= A[i] <= 10000 
#  
#  Related Topics Array Greedy


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def prevPermOpt1(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        n = len(A)
        if n==1: return A
        i = n-2
        while i>=0 and A[i] <= A[i+1]: i -= 1
        if i<0: return A
        j = i+1
        while j+1<n and A[j+1] > A[j] and A[j+1]< A[i]: j += 1
        A[i], A[j] = A[j], A[i]
        return A
        
# leetcode submit region end(Prohibit modification and deletion)
