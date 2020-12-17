#Given a time represented in the format "HH:MM", form the next closest time by r
#eusing the current digits. There is no limit on how many times a digit can be re
#used. 
#
# You may assume the given input string is always valid. For example, "01:34", "
#12:09" are all valid. "1:34", "12:9" are all invalid. 
#
# Example 1:
# 
#Input: "19:34"
#Output: "19:39"
#Explanation: The next closest time choosing from digits 1, 9, 3, 4, is 19:39, w
#hich occurs 5 minutes later.  It is not 19:33, because this occurs 23 hours and 
#59 minutes later.
# 
# 
#
# Example 2:
# 
#Input: "23:59"
#Output: "22:22"
#Explanation: The next closest time choosing from digits 2, 3, 5, 9, is 22:22. I
#t may be assumed that the returned time is next day's time since it is smaller t
#han the input time numerically.
# 
# Related Topics String




#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def nextClosestTime(self, time):
        """
        :type time: str
        :rtype: str
        """
        nums = set()
        for i in [0,1,3,4]: nums.add(int(time[i]))
        self.h0 = int(time[0:2])
        self.m0 = int(time[3:5])
        self.best_h = self.h0
        self.best_m = self.m0
        self.dfs([], nums)
        return '%02d:%02d'%(self.best_h, self.best_m)

    def dfs(self, cur, nums):
        if len(cur)==4:
            h = cur[0]*10+cur[1]
            m = cur[2]*10+cur[3]
            if h>23 or m>59:return
            if self.timediff(h, m, self.h0, self.m0) < self.timediff(self.best_h, self.best_m, self.h0, self.m0):
                self.best_h = h
                self.best_m = m
            return
        for num in nums:
            self.dfs(cur+[num], nums)

    def timediff(self, h1, m1, h2, m2):
        if h1==h2 and m1==m2: return 60*24
        return (h1*60+m1-h2*60-m2+60*24)%(60*24)

        
#leetcode submit region end(Prohibit modification and deletion)
