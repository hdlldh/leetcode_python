# Find the smallest prime palindrome greater than or equal to N. 
# 
#  Recall that a number is prime if it's only divisors are 1 and itself, and it 
# is greater than 1. 
# 
#  For example, 2,3,5,7,11 and 13 are primes. 
# 
#  Recall that a number is a palindrome if it reads the same from left to right 
# as it does from right to left. 
# 
#  For example, 12321 is a palindrome. 
# 
#  
# 
#  
#  Example 1: 
# 
#  
# Input: 6
# Output: 7
#  
# 
#  
#  Example 2: 
# 
#  
# Input: 8
# Output: 11
#  
# 
#  
#  Example 3: 
# 
#  
# Input: 13
# Output: 101 
#  
#  
#  
# 
#  
# 
#  Note: 
# 
#  
#  1 <= N <= 10^8 
#  The answer is guaranteed to exist and be less than 2 * 10^8. 
#  
#  Related Topics Math


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def primePalindrome(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N>=8 and N<=11: return 11

        def is_prime(n):
            if n < 2: return False
            if n == 2: return True
            for i in range(2, int(n ** 0.5) + 1):
                if n % i == 0: return False
            return True

        for i in xrange(1, 100000):
            s = str(i)
            rev = ''.join([x for x in reversed(s)])
            j = int(s+rev[1:])
            if j>=N and is_prime(j): return j
        return -1
        
# leetcode submit region end(Prohibit modification and deletion)
