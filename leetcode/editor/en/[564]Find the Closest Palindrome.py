# Given an integer n, find the closest integer (not including itself), which is 
# a palindrome. 
# 
#  The 'closest' is defined as absolute difference minimized between two integer
# s. 
# 
#  Example 1: 
#  
# Input: "123"
# Output: "121"
#  
#  
# 
#  Note: 
#  
#  The input n is a positive integer represented by string, whose length will no
# t exceed 18. 
#  If there is a tie, return the smaller one as answer. 
#  
#  Related Topics String


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def nearestPalindromic(self, n):
        """
        :type n: str
        :rtype: str
        """
        l = len(n)
        mem = set()
        mem.add(10 ** l + 1)
        mem.add(10 ** (l - 1) - 1)
        prefix = int(n[:(l + 1) // 2])
        for k in range(-1, 2):
            pre = str(prefix + k)
            if l % 2 == 0:
                mem.add(int(pre + pre[::-1]))
            else:
                mem.add(int(pre + pre[:-1][::-1]))

        if int(n) in mem: mem.remove(int(n))
        ans = None
        diff = float('inf')
        for num in mem:
            if abs(num - int(n)) < diff:
                diff = abs(num - int(n))
                ans = num
            elif abs(num - int(n)) == diff:
                ans = min(ans, num)
        return str(ans)
        
# leetcode submit region end(Prohibit modification and deletion)
