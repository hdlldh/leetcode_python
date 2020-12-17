# We are given a list of (axis-aligned) rectangles. Each rectangle[i] = [x1, y1,
#  x2, y2] , where (x1, y1) are the coordinates of the bottom-left corner, and (x2
# , y2) are the coordinates of the top-right corner of the ith rectangle. 
# 
#  Find the total area covered by all rectangles in the plane. Since the answer 
# may be too large, return it modulo 10^9 + 7. 
# 
#  
# 
#  Example 1: 
# 
#  
# Input: [[0,0,2,2],[1,0,2,3],[1,0,3,1]]
# Output: 6
# Explanation: As illustrated in the picture.
#  
# 
#  Example 2: 
# 
#  
# Input: [[0,0,1000000000,1000000000]]
# Output: 49
# Explanation: The answer is 10^18 modulo (10^9 + 7), which is (10^9)^2 = (-7)^2
#  = 49.
#  
# 
#  Note: 
# 
#  
#  1 <= rectangles.length <= 200 
#  rectanges[i].length = 4 
#  0 <= rectangles[i][j] <= 10^9 
#  The total area covered by all rectangles will never exceed 2^63 - 1 and thus 
# will fit in a 64-bit signed integer. 
#  Related Topics Segment Tree Line Sweep


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def rectangleArea(self, rectangles):
        """
        :type rectangles: List[List[int]]
        :rtype: int
        """
        events = []
        modulos = 1000000007
        for x1, y1, x2, y2 in rectangles:
            events.append([x1, 0, y1, y2])
            events.append([x2, 1, y1, y2])

        events.sort()
        active = []
        ans = 0

        def get_y(active):
            ans = 0
            cur = -float('inf')
            for y1, y2 in active:
                cur = max(cur, y1)
                ans += max(0, y2 - cur)
                cur = max(cur, y2)
            return ans

        prev_x = events[0][0]
        for x, status, y1, y2 in events:
            ans += (x - prev_x) * get_y(active) % modulos
            if status == 0:
                active.append((y1, y2))
            else:
                active.remove((y1, y2))
            active.sort()
            prev_x = x
        return ans % modulos
        
# leetcode submit region end(Prohibit modification and deletion)
