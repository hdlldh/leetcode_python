# N cars are going to the same destination along a one lane road. The destinatio
# n is target miles away. 
# 
#  Each car i has a constant speed speed[i] (in miles per hour), and initial pos
# ition position[i] miles towards the target along the road. 
# 
#  A car can never pass another car ahead of it, but it can catch up to it, and 
# drive bumper to bumper at the same speed. 
# 
#  The distance between these two cars is ignored - they are assumed to have the
#  same position. 
# 
#  A car fleet is some non-empty set of cars driving at the same position and sa
# me speed. Note that a single car is also a car fleet. 
# 
#  If a car catches up to a car fleet right at the destination point, it will st
# ill be considered as one car fleet. 
# 
#  
# How many car fleets will arrive at the destination? 
# 
#  
# 
#  Example 1: 
# 
#  
# Input: target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]
# Output: 3
# Explanation:
# The cars starting at 10 and 8 become a fleet, meeting each other at 12.
# The car starting at 0 doesn't catch up to any other car, so it is a fleet by i
# tself.
# The cars starting at 5 and 3 become a fleet, meeting each other at 6.
# Note that no other cars meet these fleets before the destination, so the answe
# r is 3.
#  
# 
#  
# Note: 
# 
#  
#  0 <= N <= 10 ^ 4 
#  0 < target <= 10 ^ 6 
#  0 < speed[i] <= 10 ^ 6 
#  0 <= position[i] < target 
#  All initial positions are different. 
#  Related Topics Sort


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """
        cars = sorted(zip(position, speed))
        times = [float(target - p) / s for p, s in cars]
        ans = 0
        N = len(times)
        stack = []
        for i in range(N - 1, -1, -1):
            while stack and times[i] > stack[-1]:
                stack.pop()
            if not stack:
                ans += 1
                stack.append(times[i])

        return ans
# leetcode submit region end(Prohibit modification and deletion)
