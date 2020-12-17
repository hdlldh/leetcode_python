#A sorted list A contains 1, plus some number of primes. Then, for every p < q in the list, we consider the fraction p/q. 
#
# What is the K-th smallest fraction considered? Return your answer as an array of ints, where answer[0] = p and answer[1] = q. 
#
# 
#Examples:
#Input: A = [1, 2, 3, 5], K = 3
#Output: [2, 5]
#Explanation:
#The fractions to be considered in sorted order are:
#1/5, 1/3, 2/5, 1/2, 3/5, 2/3.
#The third fraction is 2/5.
#
#Input: A = [1, 7], K = 1
#Output: [1, 7]
# 
#
# Note: 
#
# 
# A will have length between 2 and 2000. 
# Each A[i] will be between 1 and 30000. 
# K will be between 1 and A.length * (A.length - 1) / 2. 
# Related Topics Binary Search Heap



#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def kthSmallestPrimeFraction(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: List[int]
        """
        n = len(A)
        low = 0.0
        high = 1.0
        while (high-low)>1e-9:
            mid = (low+high)*0.5
            count, i, j = self.under(A, mid)
            if count > K: high = mid
            elif count <K: low = mid
            else: return [A[i],A[j]]
        return

    def under(self, A, m):
        n = len(A)
        j= 1
        count = 0
        best = 0.0
        best_i = 0
        best_j = 0
        for i in range(n):
            while j<n and A[i] > A[j]*m: j+=1
            count += n -j
            if j==n: break
            if A[i]>A[j]*best:
                best = A[i]*1.0/A[j]
                best_i = i
                best_j = j
        return count, best_i, best_j
#leetcode submit region end(Prohibit modification and deletion)
