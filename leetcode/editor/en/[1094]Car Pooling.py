# You are driving a vehicle that has capacity empty seats initially available fo
# r passengers. The vehicle only drives east (ie. it cannot turn around and drive 
# west.) 
# 
#  Given a list of trips, trip[i] = [num_passengers, start_location, end_locatio
# n] contains information about the i-th trip: the number of passengers that must 
# be picked up, and the locations to pick them up and drop them off. The locations
#  are given as the number of kilometers due east from your vehicle's initial loca
# tion. 
# 
#  Return true if and only if it is possible to pick up and drop off all passeng
# ers for all the given trips. 
# 
#  
# 
#  Example 1: 
# 
#  
# Input: trips = [[2,1,5],[3,3,7]], capacity = 4
# Output: false
#  
# 
#  
#  Example 2: 
# 
#  
# Input: trips = [[2,1,5],[3,3,7]], capacity = 5
# Output: true
#  
# 
#  
#  Example 3: 
# 
#  
# Input: trips = [[2,1,5],[3,5,7]], capacity = 3
# Output: true
#  
# 
#  
#  Example 4: 
# 
#  
# Input: trips = [[3,2,7],[3,7,9],[8,3,9]], capacity = 11
# Output: true
#  
#  
#  
#  
# 
#  
#  
#  
#  
#  
#  
#  
# 
#  
#  Constraints: 
# 
#  
#  trips.length <= 1000 
#  trips[i].length == 3 
#  1 <= trips[i][0] <= 100 
#  0 <= trips[i][1] < trips[i][2] <= 1000 
#  1 <= capacity <= 100000 
#  
#  Related Topics Greedy


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def carPooling(self, trips, capacity):
        """
        :type trips: List[List[int]]
        :type capacity: int
        :rtype: bool
        """
        events = []
        for n, start, end in trips:
            events.append([start, n])
            events.append([end, -n])
        events.sort()
        count = 0
        for event, n in events:
            count += n
            if n> 0 and count > capacity: return False
        return True
# leetcode submit region end(Prohibit modification and deletion)
