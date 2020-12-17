# In an exam room, there are N seats in a single row, numbered 0, 1, 2, ..., N-1
# . 
# 
#  When a student enters the room, they must sit in the seat that maximizes the 
# distance to the closest person. If there are multiple such seats, they sit in th
# e seat with the lowest number. (Also, if no one is in the room, then the student
#  sits at seat number 0.) 
# 
#  Return a class ExamRoom(int N) that exposes two functions: ExamRoom.seat() re
# turning an int representing what seat the student sat in, and ExamRoom.leave(int
#  p) representing that the student in seat number p now leaves the room. It is gu
# aranteed that any calls to ExamRoom.leave(p) have a student sitting in seat p. 
# 
#  
# 
#  Example 1: 
# 
#  
# Input: ["ExamRoom","seat","seat","seat","seat","leave","seat"], [[10],[],[],[]
# ,[],[4],[]]
# Output: [null,0,9,4,2,null,5]
# Explanation:
# ExamRoom(10) -> null
# seat() -> 0, no one is in the room, then the student sits at seat number 0.
# seat() -> 9, the student sits at the last seat number 9.
# seat() -> 4, the student sits at the last seat number 4.
# seat() -> 2, the student sits at the last seat number 2.
# leave(4) -> null
# seat() -> 5, the student sits at the last seat number 5.
#  
# 
#  
# 
#  Note: 
# 
#  
#  1 <= N <= 10^9 
#  ExamRoom.seat() and ExamRoom.leave() will be called at most 10^4 times across
#  all test cases. 
#  Calls to ExamRoom.leave(p) are guaranteed to have a student currently sitting
#  in seat number p. 
#  
#  Related Topics Ordered Map

import bisect
# leetcode submit region begin(Prohibit modification and deletion)
class ExamRoom(object):

    def __init__(self, N):
        """
        :type N: int
        """
        self.N = N
        self.seats = []

    def seat(self):
        """
        :rtype: int
        """
        if not self.seats:
            self.seats.append(0)
            return 0
        dmax = -1
        s = None
        if self.seats[0]!= 0:
            d = self.seats[0]
            if d > dmax:
                dmax = d
                s = 0

        for i in range(1, len(self.seats)):
            if self.seats[i-1]+1 == self.seats[i]:continue
            mid = (self.seats[i-1]+self.seats[i])/2
            d = mid - self.seats[i-1]
            if d>dmax:
                dmax = d
                s = mid

        if self.seats[-1]!=self.N-1:
            d = self.N -1 - self.seats[-1]
            if d> dmax:
                dmax = d
                s = self.N-1
        bisect.insort(self.seats, s)
        

    def leave(self, p):
        """
        :type p: int
        :rtype: None
        """
        idx = bisect.bisect_left(self.seats, p)
        if idx<len(self.seats) and self.seats[idx] == p:
            self.seats = self.seat[:idx] + self.seats[idx+1:]
        


# Your ExamRoom object will be instantiated and called as such:
# obj = ExamRoom(N)
# param_1 = obj.seat()
# obj.leave(p)
# leetcode submit region end(Prohibit modification and deletion)
