# Given the availability time slots arrays slots1 and slots2 of two people and a
#  meeting duration duration, return the earliest time slot that works for both of
#  them and is of duration duration. 
# 
#  If there is no common time slot that satisfies the requirements, return an em
# pty array. 
# 
#  The format of a time slot is an array of two elements [start, end] representi
# ng an inclusive time range from start to end. 
# 
#  It is guaranteed that no two availability slots of the same person intersect 
# with each other. That is, for any two time slots [start1, end1] and [start2, end
# 2] of the same person, either start1 > end2 or start2 > end1. 
# 
#  
#  Example 1: 
# 
#  
# Input: slots1 = [[10,50],[60,120],[140,210]], slots2 = [[0,15],[60,70]], durat
# ion = 8
# Output: [60,68]
#  
# 
#  Example 2: 
# 
#  
# Input: slots1 = [[10,50],[60,120],[140,210]], slots2 = [[0,15],[60,70]], durat
# ion = 12
# Output: []
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= slots1.length, slots2.length <= 10^4 
#  slots1[i].length, slots2[i].length == 2 
#  slots1[i][0] < slots1[i][1] 
#  slots2[i][0] < slots2[i][1] 
#  0 <= slots1[i][j], slots2[i][j] <= 10^9 
#  1 <= duration <= 10^6 
#  
#  Related Topics Line Sweep


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def minAvailableDuration(self, slots1, slots2, duration):
        """
        :type slots1: List[List[int]]
        :type slots2: List[List[int]]
        :type duration: int
        :rtype: List[int]
        """
        slots1.sort()
        slots2.sort()
        m = len(slots1)
        n = len(slots2)
        i = 0
        j = 0
        while i < m and j < n:
            slot1 = slots1[i]
            slot2 = slots2[j]
            if self.get_overlap(slot1, slot2) >= duration:
                return [max(slot1[0], slot2[0]), max(slot1[0], slot2[0]) + duration]
            if slot1[0] < slot2[0]:
                i += 1
            else:
                j += 1
        return []

    def get_overlap(self, slot1, slot2):
        return max(0, min(slot1[1], slot2[1]) - max(slot1[0], slot2[0]))

    # leetcode submit region end(Prohibit modification and deletion)
