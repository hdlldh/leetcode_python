#Given integers n and k, find the lexicographically k-th smallest integer in the range from 1 to n.
#
# Note: 1 ≤ k ≤ n ≤ 109. 
#
# Example:
# 
#Input:
#n: 13   k: 2
#
#Output:
#10
#
#Explanation:
#The lexicographical order is [1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9], so the second smallest number is 10.
# 
# 
#



#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def findKthNumber(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        cur = 1
        k -= 1
        while k>0:
            gap = self.findGap(cur, cur+1, n)
            if gap<=k:
                cur += 1
                k -= gap
            else:
                cur *= 10
                k -= 1
        return cur

    def findGap(self, p, q, n):
        gap = 0
        while p<=n:
            gap += max(0, min(q,n+1)-p)
            p*=10
            q*=10
        return gap

#leetcode submit region end(Prohibit modification and deletion)
