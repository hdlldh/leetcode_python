# In a given integer array A, we must move every element of A to either list B o
# r list C. (B and C initially start empty.) 
# 
#  Return true if and only if after such a move, it is possible that the average
#  value of B is equal to the average value of C, and B and C are both non-empty. 
# 
# 
#  
# Example :
# Input: 
# [1,2,3,4,5,6,7,8]
# Output: true
# Explanation: We can split the array into [1,4,5,8] and [2,3,6,7], and both of 
# them have the average of 4.5.
#  
# 
#  Note: 
# 
#  
#  The length of A will be in the range [1, 30]. 
#  A[i] will be in the range of [0, 10000]. 
#  
# 
#  
#  Related Topics Math


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def splitArraySameAverage(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        n = len(A)
        s = sum(A)
        possible = False
        for k in range(1, n // 2 + 1):
            if (s * k) % n == 0:
                possible = True
                break
        if not possible: return False

        dp = collections.defaultdict(set)
        dp[0].add(0)
        for num in A:
            for i in xrange(n // 2 + 1, 0, -1):
                # for i in xrange(1, n//2+2):
                for a in dp[i - 1]:
                    dp[i].add(a + num)

        for k in range(1, n // 2 + 1):
            if s * k % n == 0:
                s1 = s * k // n
                if s1 in dp[k]: return True
        return False
        
# leetcode submit region end(Prohibit modification and deletion)
