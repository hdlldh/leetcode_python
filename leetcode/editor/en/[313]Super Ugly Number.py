#Write a program to find the nth super ugly number. 
#
# Super ugly numbers are positive numbers whose all prime factors are in the given prime list primes of size k. 
#
# Example: 
#
# 
#Input: n = 12, primes = [2,7,13,19]
#Output: 32 
#Explanation: [1,2,4,7,8,13,14,16,19,26,28,32] is the sequence of the first 12 
#             super ugly numbers given primes = [2,7,13,19] of size 4. 
#
# Note: 
#
# 
# 1 is a super ugly number for any given primes. 
# The given numbers in primes are in ascending order. 
# 0 < k ≤ 100, 0 < n ≤ 106, 0 < primes[i] < 1000. 
# The nth super ugly number is guaranteed to fit in a 32-bit signed integer. 
# 
# Related Topics Math Heap


import heapq
#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        heap = [1]
        visited = set()
        visited.add(1)
        for i in range(n):
            num = heapq.heappop(heap)
            if i==n-1: break
            for p in primes:
                q = num*p
                if q not in visited:
                    heapq.heappush(heap, q)
                    visited.add(q)
        return num
#leetcode submit region end(Prohibit modification and deletion)
