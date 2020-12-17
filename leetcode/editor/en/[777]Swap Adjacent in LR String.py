# In a string composed of 'L', 'R', and 'X' characters, like "RXXLRXRXL", a move
#  consists of either replacing one occurrence of "XL" with "LX", or replacing one
#  occurrence of "RX" with "XR". Given the starting string start and the ending st
# ring end, return True if and only if there exists a sequence of moves to transfo
# rm one string to the other. 
# 
#  Example: 
# 
#  
# Input: start = "RXXLRXRXL", end = "XRLXXRRLX"
# Output: True
# Explanation:
# We can transform start to end following these steps:
# RXXLRXRXL ->
# XRXLRXRXL ->
# XRLXRXRXL ->
# XRLXXRRXL ->
# XRLXXRRLX
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= len(start) == len(end) <= 10000. 
#  Both start and end will only consist of characters in {'L', 'R', 'X'}. 
#  
#  Related Topics Brainteaser


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def canTransform(self, start, end):
        """
        :type start: str
        :type end: str
        :rtype: bool
        """
        n = len(start)
        m = len(end)
        if n!=m:return False
        if start==end: return True
        if start.replace('X',"")!=end.replace('X',""):return False

        cntL = 0
        cntR = 0
        for i in range(n-1, -1, -1):
            if start[i] == 'L': cntL += 1
            if end[i] == 'L': cntL -= 1
            if cntL <0: return False

        for i in range(n):
            if start[i]== 'R': cntR += 1
            if end[i] =='R': cntR -= 1
            if cntR<0: return False
        return True
# leetcode submit region end(Prohibit modification and deletion)
