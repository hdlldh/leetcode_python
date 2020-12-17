# Given two numbers, hour and minutes. Return the smaller angle (in degrees) for
# med between the hour and the minute hand. 
# 
#  
#  Example 1: 
# 
#  
# 
#  
# Input: hour = 12, minutes = 30
# Output: 165
#  
# 
#  Example 2: 
# 
#  
# 
#  
# Input: hour = 3, minutes = 30
# Output: 75
#  
# 
#  Example 3: 
# 
#  
# 
#  
# Input: hour = 3, minutes = 15
# Output: 7.5
#  
# 
#  Example 4: 
# 
#  
# Input: hour = 4, minutes = 50
# Output: 155
#  
# 
#  Example 5: 
# 
#  
# Input: hour = 12, minutes = 0
# Output: 0
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= hour <= 12 
#  0 <= minutes <= 59 
#  Answers within 10^-5 of the actual value will be accepted as correct. 
#  
#  Related Topics Math


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def angleClock(self, hour, minutes):
        """
        :type hour: int
        :type minutes: int
        :rtype: float
        """
        t1 = (hour%12)*30 + 30 * minutes / 60.0
        t2 = minutes/60.0 * 360
        delta = (t2 -t1) % 360
        if delta >180: return 360 -delta
        return delta
        
# leetcode submit region end(Prohibit modification and deletion)
