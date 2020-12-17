#We have some permutation A of [0, 1, ..., N - 1], where N is the length of A. 
#
# The number of (global) inversions is the number of i < j with 0 <= i < j < N a
#nd A[i] > A[j]. 
#
# The number of local inversions is the number of i with 0 <= i < N and A[i] > A
#[i+1]. 
#
# Return true if and only if the number of global inversions is equal to the num
#ber of local inversions. 
#
# Example 1: 
#
# 
#Input: A = [1,0,2]
#Output: true
#Explanation: There is 1 global inversion, and 1 local inversion.
# 
#
# Example 2: 
#
# 
#Input: A = [1,2,0]
#Output: false
#Explanation: There are 2 global inversions, and 1 local inversion.
# 
#
# Note: 
#
# 
# A will be a permutation of [0, 1, ..., A.length - 1]. 
# A will have length in range [1, 5000]. 
# The time limit for this problem has been reduced. 
# 
# Related Topics Array Math




#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def isIdealPermutation(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        for i, num in enumerate(A):
            if abs(num-i)>1: return False
        return True

    def isIdealPermutation2(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        n = len(A)
        localVar = 0
        for i in range(1, n):
            if A[i-1]>A[i]: localVar += 1
        tmp = [0]*n

        def mergeSort(A, l, r, tmp):
            if l >= r: return 0
            m = l + (r - l) // 2
            ans = mergeSort(A, l, m, tmp) + mergeSort(A, m + 1, r, tmp)
            i = l
            j = m + 1
            k = l
            while i <= m and j <= r:
                if (A[i] <= A[j]):
                    tmp[k] = A[i]
                    i += 1
                    k += 1
                else:
                    tmp[k] = A[j]
                    ans += m - i + 1
                    j += 1
                    k += 1
            while i <= m:
                tmp[k] = A[i]
                i += 1
                k += 1
            while j <= r:
                tmp[k] = A[j]
                j += 1
                k += 1
            for i in range(l, r + 1): A[i] = tmp[i]
            return ans
        globalVar = mergeSort(A, 0, n - 1, tmp)
        return localVar==globalVar




        
#leetcode submit region end(Prohibit modification and deletion)
