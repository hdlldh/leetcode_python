#
#There is a strange printer with the following two special requirements:
#
# 
# The printer can only print a sequence of the same character each time. 
# At each turn, the printer can print new characters starting from and ending at any places, and will cover the original existing characters. 
# 
#
# 
#
# 
#Given a string consists of lower English letters only, your job is to count the minimum number of turns the printer needed in order to print it.
# 
#
# Example 1: 
# 
#Input: "aaabbb"
#Output: 2
#Explanation: Print "aaa" first and then print "bbb".
# 
# 
#
# Example 2: 
# 
#Input: "aba"
#Output: 2
#Explanation: Print "aaa" first and then print "b" from the second place of the string, which will cover the existing character 'a'.
# 
# 
#
# Hint: Length of the given string will not exceed 100. Related Topics Dynamic Programming Depth-first Search



#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def strangePrinter(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        return self.helper(s, {})

    def helper(self, s, mem):
        if s in mem: return mem[s]
        n = len(s)
        if n<=1: return n
        ans = self.helper(s[:-1],mem) + 1
        for i in range(n-1):
            if s[i] == s[n-1]:
                ans = min(ans, self.helper(s[:i+1], mem) + self.helper(s[i+1:n-1], mem))
        mem[s] = ans
        return ans



        
#leetcode submit region end(Prohibit modification and deletion)
