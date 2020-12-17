# Given a date, return the corresponding day of the week for that date. 
# 
#  The input is given as three integers representing the day, month and year res
# pectively. 
# 
#  Return the answer as one of the following values {"Sunday", "Monday", "Tuesda
# y", "Wednesday", "Thursday", "Friday", "Saturday"}. 
# 
#  
#  Example 1: 
# 
#  
# Input: day = 31, month = 8, year = 2019
# Output: "Saturday"
#  
# 
#  Example 2: 
# 
#  
# Input: day = 18, month = 7, year = 1999
# Output: "Sunday"
#  
# 
#  Example 3: 
# 
#  
# Input: day = 15, month = 8, year = 1993
# Output: "Sunday"
#  
# 
#  
#  Constraints: 
# 
#  
#  The given dates are valid dates between the years 1971 and 2100. 
#  Related Topics Array


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def dayOfTheWeek(self, day, month, year):
        """
        :type day: int
        :type month: int
        :type year: int
        :rtype: str
        """
        days = {6:"Sunday", 0:"Monday", 1:"Tuesday", 2:"Wednesday",
                3:"Thursday", 4:"Friday", 5:"Saturday"}
        today = datetime.datetime(year,month,day)
        return days[today.weekday()]
        
# leetcode submit region end(Prohibit modification and deletion)
