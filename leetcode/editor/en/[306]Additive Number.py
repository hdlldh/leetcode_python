#Additive number is a string whose digits can form additive sequence. 
#
# A valid additive sequence should contain at least three numbers. Except for the first two numbers, each subsequent number in the sequence must be the sum of the preceding two. 
#
# Given a string containing only digits '0'-'9', write a function to determine if it's an additive number. 
#
# Note: Numbers in the additive sequence cannot have leading zeros, so sequence 1, 2, 03 or 1, 02, 3 is invalid. 
#
# 
# Example 1: 
#
# 
#Input: "112358"
#Output: true
#Explanation: The digits can form an additive sequence: 1, 1, 2, 3, 5, 8. 
#             1 + 1 = 2, 1 + 2 = 3, 2 + 3 = 5, 3 + 5 = 8
# 
#
# Example 2: 
#
# 
#Input: "199100199"
#Output: true
#Explanation: The additive sequence is: 1, 99, 100, 199. 
#             1 + 99 = 100, 99 + 100 = 199
# 
#
# 
# Constraints: 
#
# 
# num consists only of digits '0'-'9'. 
# 1 <= num.length <= 35 
# 
#
# Follow up: 
#How would you handle overflow for very large input integers? 
# Related Topics Backtracking



#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """

        def isValid(x1, x2, start, num):
            if start == len(num): return True
            if start > len(num): return False
            sm = x1 + x2
            x1, x2 = x2, sm
            sm = str(sm)
            return isValid(x1, x2, start + len(sm), num) and num[start:start + len(sm)] == sm

        if not num: return False
        n = len(num)

        for i in range(1, n):
            x1 = num[:i]
            if x1[0] == '0' and i > 1: continue
            x1 = int(x1)
            for j in range(i + 1, n):
                x2 = num[i:j]
                if x2[0] == '0' and j > i + 1: continue
                x2 = int(x2)
                if isValid(x1, x2, j, num):
                    return True

        return False
        
#leetcode submit region end(Prohibit modification and deletion)
