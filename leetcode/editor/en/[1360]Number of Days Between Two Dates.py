# Write a program to count the number of days between two dates. 
# 
#  The two dates are given as strings, their format is YYYY-MM-DD as shown in th
# e examples. 
# 
#  
#  Example 1: 
#  Input: date1 = "2019-06-29", date2 = "2019-06-30"
# Output: 1
#  Example 2: 
#  Input: date1 = "2020-01-15", date2 = "2019-12-31"
# Output: 15
#  
#  
#  Constraints: 
# 
#  
#  The given dates are valid dates between the years 1971 and 2100. 
#  
# 


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def daysBetweenDates(self, date1, date2):
        """
        :type date1: str
        :type date2: str
        :rtype: int
        """
        y1, m1, d1 = map(int, date1.split('-'))
        y2, m2, d2 = map(int, date2.split('-'))
        return abs(int((datetime.datetime(y1, m1, d1) - datetime.datetime(y2, m2, d2)).days))

    # leetcode submit region end(Prohibit modification and deletion)
