# Given two non-negative integers num1 and num2 represented as string, return th
# e sum of num1 and num2. 
# 
#  Note:
#  
#  The length of both num1 and num2 is < 5100. 
#  Both num1 and num2 contains only digits 0-9. 
#  Both num1 and num2 does not contain any leading zero. 
#  You must not use any built-in BigInteger library or convert the inputs to int
# eger directly. 
#  
#  Related Topics String


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        m = len(num1)
        n = len(num2)
        xlist = list(num1)
        ylist = list(num2)
        xlist.reverse()
        ylist.reverse()
        c = 0
        ans = []
        for i in range(max(m, n)):
            x = int(xlist[i]) if i < m else 0
            y = int(ylist[i]) if i < n else 0
            ans.append(str((x + y + c) % 10))
            c = 1 if (x + y + c) >= 10 else 0
        if c: ans.append('1')
        ans.reverse()
        return ''.join(ans)
# leetcode submit region end(Prohibit modification and deletion)
