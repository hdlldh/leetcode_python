#Given an m x n matrix of positive integers representing the height of each unit cell in a 2D elevation map, compute the volume of water it is able to trap after raining. 
#
# 
#
# Note: 
#
# Both m and n are less than 110. The height of each unit cell is greater than 0 and is less than 20,000. 
#
# 
#
# Example: 
#
# 
#Given the following 3x6 height map:
#[
#  [1,4,3,1,3,2],
#  [3,2,1,3,2,4],
#  [2,3,3,2,3,1]
#]
#
#Return 4.
# 
#
# 
#
# The above image represents the elevation map [[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]] before the rain. 
#
# 
#
# 
#
# After the rain, water is trapped between the blocks. The total volume of water trapped is 4. 
# Related Topics Heap Breadth-first Search



#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def trapRainWater(self, heightMap):
        """
        :type heightMap: List[List[int]]
        :rtype: int
        """
        ans = 0
        m = len(heightMap)
        if m==0: return ans
        n = len(heightMap[0])
        mxH = -float('inf')
        pq = []
        seen = set()
        for i in range(m):
            for j in range(n):
                if i in [0, m-1] or j in [0, n-1]:
                    heapq.heappush(pq, [heightMap[i][j], i, j])
                    seen.add((i, j))
        dirs = [-1, 0, 1, 0, -1]
        while pq:
            h, i, j = heapq.heappop(pq)
            mxH = max(mxH, h)
            for k in range(4):
                ti = i+dirs[k]
                tj = j+dirs[k+1]
                if ti<0 or ti>=m or tj<0 or tj>=n: continue
                if (ti, tj) in seen: continue
                ans += max(0, mxH-heightMap[ti][tj])
                heapq.heappush(pq, [heightMap[ti][tj], ti, tj])
                seen.add((ti, tj))
        return ans


        
#leetcode submit region end(Prohibit modification and deletion)
