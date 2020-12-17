# You have some sticks with positive integer lengths. 
# 
#  You can connect any two sticks of lengths X and Y into one stick by paying a 
# cost of X + Y. You perform this action until there is one stick remaining. 
# 
#  Return the minimum cost of connecting all the given sticks into one stick in 
# this way. 
# 
#  
#  Example 1: 
#  Input: sticks = [2,4,3]
# Output: 14
#  Example 2: 
#  Input: sticks = [1,8,3,5]
# Output: 30
#  
#  
#  Constraints: 
# 
#  
#  1 <= sticks.length <= 10^4 
#  1 <= sticks[i] <= 10^4 
#  
#  Related Topics Greedy
import heapq

# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def connectSticks(self, sticks):
        """
        :type sticks: List[int]
        :rtype: int
        """
        heapq.heapify(sticks)
        ans = 0
        while len(sticks)>1:
            p = heapq.heappop(sticks)
            q = heapq.heappop(sticks)
            ans += p+q
            heapq.heappush(sticks, p+q)
        return ans
        
# leetcode submit region end(Prohibit modification and deletion)
