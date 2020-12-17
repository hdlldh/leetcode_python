#
#Nearly every one have used the Multiplication Table. But could you find out the k-th smallest number quickly from the multiplication table?
# 
#
# 
#Given the height m and the length n of a m * n Multiplication Table, and a positive integer k, you need to return the k-th smallest number in this table.
# 
#
# Example 1: 
# 
#Input: m = 3, n = 3, k = 5
#Output: 
#Explanation: 
#The Multiplication Table:
#1	2	3
#2	4	6
#3	6	9
#
#The 5-th smallest number is 3 (1, 2, 2, 3, 3).
# 
# 
#
#
# Example 2: 
# 
#Input: m = 2, n = 3, k = 6
#Output: 
#Explanation: 
#The Multiplication Table:
#1	2	3
#2	4	6
#
#The 6-th smallest number is 6 (1, 2, 2, 3, 4, 6).
# 
# 
#
#
# Note: 
# 
# The m and n will be in the range [1, 30000]. 
# The k will be in the range [1, m * n] 
# 
# Related Topics Binary Search



#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def findKthNumber(self, m, n, k):
        """
        :type m: int
        :type n: int
        :type k: int
        :rtype: int
        """
        low = 1
        high = m*n
        while low<=high:
            mid = low+(high-low)/2
            count = self.under(m, n, mid)
            if count >= k: high = mid-1
            else: low = mid +1
        return low

    def under(self, m, n, v):
        j = n
        count = 0
        for i in range(1, m+1):
            while j>=1 and i*j>v: j-=1
            if j==-1: break
            count += j
        return count

#leetcode submit region end(Prohibit modification and deletion)
