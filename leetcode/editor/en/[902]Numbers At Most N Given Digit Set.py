#We have a sorted set of digits D, a non-empty subset of {'1','2','3','4','5','6
#','7','8','9'}. (Note that '0' is not included.) 
#
# Now, we write numbers using these digits, using each digit as many times as we
# want. For example, if D = {'1','3','5'}, we may write numbers such as '13', '55
#1', '1351315'. 
#
# Return the number of positive integers that can be written (using the digits o
#f D) that are less than or equal to N. 
#
# 
#
# Example 1: 
#
# 
#Input: D = ["1","3","5","7"], N = 100
#Output: 20
#Explanation: 
#The 20 numbers that can be written are:
#1, 3, 5, 7, 11, 13, 15, 17, 31, 33, 35, 37, 51, 53, 55, 57, 71, 73, 75, 77.
# 
#
# 
# Example 2: 
#
# 
#Input: D = ["1","4","9"], N = 1000000000
#Output: 29523
#Explanation: 
#We can write 3 one digit numbers, 9 two digit numbers, 27 three digit numbers,
#81 four digit numbers, 243 five digit numbers, 729 six digit numbers,
#2187 seven digit numbers, 6561 eight digit numbers, and 19683 nine digit number
#s.
#In total, this is 29523 integers that can be written using the digits of D. 
# 
#
# 
#
# Note: 
#
# 
# D is a subset of digits '1'-'9' in sorted order. 
# 1 <= N <= 10^9 
# 
# Related Topics Math Dynamic Programming




#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def atMostNGivenDigitSet(self, D, N):
        """
        :type D: List[str]
        :type N: int
        :rtype: int
        """
        size = len(D)
        strN = str(N)
        lenN = len(strN)
        ans = sum([size**i for i in range(1, lenN)])
        for i, c in enumerate(strN):
            for d in D:
                if d< strN[i]: ans += size**(lenN-i-1)
            if c not in D: return ans
        return ans+1

        
#leetcode submit region end(Prohibit modification and deletion)
