# In an infinite chess board with coordinates from -infinity to +infinity, you h
# ave a knight at square [0, 0]. 
# 
#  A knight has 8 possible moves it can make, as illustrated below. Each move is
#  two squares in a cardinal direction, then one square in an orthogonal direction
# . 
# 
#  
# 
#  Return the minimum number of steps needed to move the knight to the square [x
# , y]. It is guaranteed the answer exists. 
# 
#  
#  Example 1: 
# 
#  
# Input: x = 2, y = 1
# Output: 1
# Explanation: [0, 0] → [2, 1]
#  
# 
#  Example 2: 
# 
#  
# Input: x = 5, y = 5
# Output: 4
# Explanation: [0, 0] → [2, 1] → [4, 2] → [3, 4] → [5, 5]
#  
# 
#  
#  Constraints: 
# 
#  
#  |x| + |y| <= 300 
#  
#  Related Topics Breadth-first Search


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def minKnightMoves(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        dirs = [[1,-2],[1,2],[-1,-2],[-1,2],[2,-1],[2,1],[-2,-1],[-2,1]]
        queue = collections.deque()
        queue.append([0,0])
        visited = set()
        visited.add((0,0))
        x = x if x>=0 else -x
        y = y if y>=0 else -y
        steps = 0
        while queue:
            size = len(queue)
            for _ in range(size):
                ux, uy = queue.popleft()
                if ux == x and uy==y: return steps
                for k in range(8):
                    vx = ux+dirs[k][0]
                    vy = uy+dirs[k][1]
                    if (vx, vy) in visited or vx<=-3 or vy<=-3: continue
                    queue.append([vx, vy])
                    visited.add((vx, vy))
            steps += 1
        return steps

        
# leetcode submit region end(Prohibit modification and deletion)
