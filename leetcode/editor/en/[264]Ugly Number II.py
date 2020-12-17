#Write a program to find the n-th ugly number. 
#
# Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. 
#
# Example: 
#
# 
#Input: n = 10
#Output: 12
#Explanation: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers. 
#
# Note: 
#
# 
# 1 is typically treated as an ugly number. 
# n does not exceed 1690. 
# Related Topics Math Dynamic Programming Heap


import heapq
#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        heap = [1]
        visited = set()
        visited.add(1)
        for i in range(n):
            num = heapq.heappop(heap)
            if i == n - 1: break
            for p in [2, 3, 5]:
                q = p * num
                if q not in visited:
                    heapq.heappush(heap, q)
                    visited.add(q)
        return num
        
#leetcode submit region end(Prohibit modification and deletion)
