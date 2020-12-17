# Given an array A, we can perform a pancake flip: We choose some positive integ
# er k <= A.length, then reverse the order of the first k elements of A. We want t
# o perform zero or more pancake flips (doing them one after another in succession
# ) to sort the array A. 
# 
#  Return the k-values corresponding to a sequence of pancake flips that sort A.
#  Any valid answer that sorts the array within 10 * A.length flips will be judged
#  as correct. 
# 
#  
# 
#  Example 1: 
# 
#  
# Input: [3,2,4,1]
# Output: [4,2,4,3]
# Explanation: 
# We perform 4 pancake flips, with k values 4, 2, 4, and 3.
# Starting state: A = [3, 2, 4, 1]
# After 1st flip (k=4): A = [1, 4, 2, 3]
# After 2nd flip (k=2): A = [4, 1, 2, 3]
# After 3rd flip (k=4): A = [3, 2, 1, 4]
# After 4th flip (k=3): A = [1, 2, 3, 4], which is sorted. 
#  
# 
#  
#  Example 2: 
# 
#  
# Input: [1,2,3]
# Output: []
# Explanation: The input is already sorted, so there is no need to flip anything
# .
# Note that other answers, such as [3, 3], would also be accepted.
#  
# 
#  
#  
# 
#  Note: 
# 
#  
#  1 <= A.length <= 100 
#  A[i] is a permutation of [1, 2, ..., A.length] 
#  
#  Related Topics Array Sort


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def pancakeSort(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        n = len(A)
        if n==0: return []
        ans = []
        for i in range(n, 0, -1):
            idx = self.find_max(A, i)
            if idx == i-1: continue
            self.reverse(A, 0, idx)
            ans.append(idx+1)
            self.reverse(A, 0, i-1)
            ans.append(i)
        #print(A)

        return ans



    def find_max(self, A, n):
        ans = 0
        mx = -float('inf')
        for i in range(n):
            if A[i] > mx:
                mx = A[i]
                ans = i
        return ans

    def reverse(self, A, i, j):
        left = i
        right = j
        while left<right:
            A[left], A[right] = A[right], A[left]
            left += 1
            right -= 1

# leetcode submit region end(Prohibit modification and deletion)
