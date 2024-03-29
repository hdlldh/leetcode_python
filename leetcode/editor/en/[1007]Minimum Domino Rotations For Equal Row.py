#In a row of dominoes, A[i] and B[i] represent the top and bottom halves of the i-th domino. (A domino is a tile with two numbers from 1 to 6 - one on each half of the tile.) 
#
# We may rotate the i-th domino, so that A[i] and B[i] swap values. 
#
# Return the minimum number of rotations so that all the values in A are the same, or all the values in B are the same. 
#
# If it cannot be done, return -1. 
#
# 
#
# Example 1: 
#
# 
#
# 
#Input: A = [2,1,2,4,2,2], B = [5,2,6,2,3,2]
#Output: 2
#Explanation: 
#The first figure represents the dominoes as given by A and B: before we do any rotations.
#If we rotate the second and fourth dominoes, we can make every value in the top row equal to 2, as indicated by the second figure.
# 
#
# Example 2: 
#
# 
#Input: A = [3,5,1,2,3], B = [3,6,3,3,4]
#Output: -1
#Explanation: 
#In this case, it is not possible to rotate the dominoes to make one row of values equal.
# 
#
# 
#
# Note: 
#
# 
# 1 <= A[i], B[i] <= 6 
# 2 <= A.length == B.length <= 20000 
# 
# Related Topics Array Greedy

import collections

#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def minDominoRotations(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        n = len(A)
        count = collections.Counter(A+B)
        target = count.most_common(1)[0][0]
        if count[target]<n: return -1
        a_swap = 0
        b_swap = 0
        for i in range(n):
            if A[i] == B[i]:
                if A[i] == target: continue
                else: return -1
            else:
                if A[i] == target: b_swap+=1
                elif B[i] == target: a_swap+=1
                else: return -1
        return min(a_swap, b_swap)
        
#leetcode submit region end(Prohibit modification and deletion)
