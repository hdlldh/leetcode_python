#Write a program to find the n-th ugly number. 
#
# Ugly numbers are positive integers which are divisible by a or b or c. 
#
# 
# Example 1: 
#
# 
#Input: n = 3, a = 2, b = 3, c = 5
#Output: 4
#Explanation: The ugly numbers are 2, 3, 4, 5, 6, 8, 9, 10... The 3rd is 4. 
#
# Example 2: 
#
# 
#Input: n = 4, a = 2, b = 3, c = 4
#Output: 6
#Explanation: The ugly numbers are 2, 3, 4, 6, 8, 9, 10, 12... The 4th is 6.
# 
#
# Example 3: 
#
# 
#Input: n = 5, a = 2, b = 11, c = 13
#Output: 10
#Explanation: The ugly numbers are 2, 4, 6, 8, 10, 11, 12, 13... The 5th is 10.
# 
#
# Example 4: 
#
# 
#Input: n = 1000000000, a = 2, b = 217983653, c = 336916467
#Output: 1999999984
# 
#
# 
# Constraints: 
#
# 
# 1 <= n, a, b, c <= 10^9 
# 1 <= a * b * c <= 10^18 
# It's guaranteed that the result will be in range [1, 2 * 10^9] 
# 
# Related Topics Math Binary Search




#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def nthUglyNumber(self, n, a, b, c):
        """
        :type n: int
        :type a: int
        :type b: int
        :type c: int
        :rtype: int
        """
        ab = self.lcm(a, b)
        bc = self.lcm(b, c)
        ac = self.lcm(a, c)
        abc = self.lcm(a, bc)
        low = 1
        high = 0x7FFFFFFF
        while low<=high:
            mid = low + (high-low)//2
            count = mid//a + mid//b + mid//c - mid//ab -mid//ac -mid//bc + mid//abc
            if count>=n: high = mid -1
            elif count<n: low = mid + 1
        return low

    def gcd(self, a, b):
        if b==0: return a
        return self.gcd(b, a%b)

    def lcm(self, a, b): return a*b//self.gcd(a, b)

        
#leetcode submit region end(Prohibit modification and deletion)
