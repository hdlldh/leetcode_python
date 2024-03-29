# We have two integer sequences A and B of the same non-zero length. 
# 
#  We are allowed to swap elements A[i] and B[i]. Note that both elements are in
#  the same index position in their respective sequences. 
# 
#  At the end of some number of swaps, A and B are both strictly increasing. (A 
# sequence is strictly increasing if and only if A[0] < A[1] < A[2] < ... < A[A.le
# ngth - 1].) 
# 
#  Given A and B, return the minimum number of swaps to make both sequences stri
# ctly increasing. It is guaranteed that the given input always makes it possible.
#  
# 
#  
# Example:
# Input: A = [1,3,5,4], B = [1,2,3,7]
# Output: 1
# Explanation: 
# Swap A[3] and B[3].  Then the sequences are:
# A = [1, 3, 5, 7] and B = [1, 2, 3, 4]
# which are both strictly increasing.
#  
# 
#  Note: 
# 
#  
#  A, B are arrays with the same length, and that length will be in the range [1
# , 1000]. 
#  A[i], B[i] are integer values in the range [0, 2000]. 
#  
#  Related Topics Dynamic Programming


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def minSwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        n = len(A)
        keep = [float('inf')]*n
        keep[0]= 0
        swap = [float('inf')]*n
        swap[0] = 1
        for i in range(1, n):
            if A[i]>A[i-1] and B[i] >B[i-1]:
                keep[i] = keep[i-1]
                swap[i] = swap[i-1] +1
            if A[i]>B[i-1] and B[i]>A[i-1]:
                keep[i] = min(keep[i], swap[i-1])
                swap[i] = min(swap[i], keep[i-1]+1)
        return min(keep[-1], swap[-1])
# leetcode submit region end(Prohibit modification and deletion)
