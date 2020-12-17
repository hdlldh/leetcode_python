#A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down). 
#
# Write a function to count the total strobogrammatic numbers that exist in the range of low <= num <= high. 
#
# Example: 
#
# 
#Input: low = "50", high = "100"
#Output: 3 
#Explanation: 69, 88, and 96 are three strobogrammatic numbers. 
#
# Note: 
#Because the range might be a large number, the low and high numbers are represented as string. 
# Related Topics Math Recursion



#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def strobogrammaticInRange(self, low, high):
        """
        :type low: str
        :type high: str
        :rtype: int
        """
        self.ans = 0
        minLen = len(low)
        maxLen = len(high)
        low = int(low)
        high = int(high)
        for i in range(minLen, maxLen+1):
            self.find(low, high, "", i)
            self.find(low, high, "0", i)
            self.find(low, high, "1", i)
            self.find(low, high, "8", i)
        return self.ans

    def find(self, low, high, num, l):
        if len(num) > l: return
        if len(num) ==l:
            if l>1 and num[0]=='0': return
            if int(num) < low or int(num) > high: return
            self.ans += 1

        self.find(low, high, "0" + num + "0", l)
        self.find(low, high, "1" + num + "1", l)
        self.find(low, high, "6" + num + "9", l)
        self.find(low, high, "8" + num + "8", l)
        self.find(low, high, "9" + num + "6", l)
#leetcode submit region end(Prohibit modification and deletion)
