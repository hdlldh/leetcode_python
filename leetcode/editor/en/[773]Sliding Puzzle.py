# On a 2x3 board, there are 5 tiles represented by the integers 1 through 5, and
#  an empty square represented by 0. 
# 
#  A move consists of choosing 0 and a 4-directionally adjacent number and swapp
# ing it. 
# 
#  The state of the board is solved if and only if the board is [[1,2,3],[4,5,0]
# ]. 
# 
#  Given a puzzle board, return the least number of moves required so that the s
# tate of the board is solved. If it is impossible for the state of the board to b
# e solved, return -1. 
# 
#  Examples: 
# 
#  
# Input: board = [[1,2,3],[4,0,5]]
# Output: 1
# Explanation: Swap the 0 and the 5 in one move.
#  
# 
#  
# Input: board = [[1,2,3],[5,4,0]]
# Output: -1
# Explanation: No number of moves will make the board solved.
#  
# 
#  
# Input: board = [[4,1,2],[5,0,3]]
# Output: 5
# Explanation: 5 is the smallest number of moves that solves the board.
# An example path:
# After move 0: [[4,1,2],[5,0,3]]
# After move 1: [[4,1,2],[0,5,3]]
# After move 2: [[0,1,2],[4,5,3]]
# After move 3: [[1,0,2],[4,5,3]]
# After move 4: [[1,2,0],[4,5,3]]
# After move 5: [[1,2,3],[4,5,0]]
#  
# 
#  
# Input: board = [[3,2,4],[1,5,0]]
# Output: 14
#  
# 
#  Note: 
# 
#  
#  board will be a 2 x 3 array as described above. 
#  board[i][j] will be a permutation of [0, 1, 2, 3, 4, 5]. 
#  
#  Related Topics Breadth-first Search


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def slidingPuzzle(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        m, n = len(board), len(board[0])
        start = []
        end = []
        cnt = 1
        for i in range(m):
            for j in range(n):
                start.append(str(board[i][j]))
                if cnt != m*n:
                    end.append(str(cnt))
                    cnt +=1
                else:
                    end.append('0')
        start_str = '_'.join(start)
        end_str = '_'.join(end)
        if start_str == end_str: return 0
        s1 = set([start_str])
        s2 = set([end_str])
        visited = set([start_str, end_str])
        steps = 0
        dirs = [-1,0 ,1, 0, -1]
        while s1 and s2:
            steps += 1
            s = set()
            if len(s1)>len(s2): s1, s2 = s2, s1
            for u in s1:
                u_arr = u.split('_')
                id0 = None
                for k in range(len(u_arr)):
                    if u_arr[k]=='0':
                        id0 = k
                        break
                #print(id0)
                i0 = id0 // n
                j0 = id0 % n
                for k in range(4):
                    i1 = i0 + dirs[k]
                    j1 = j0 + dirs[k+1]
                    if i1<0 or i1>=m or j1<0 or j1>=n: continue
                    id1 = i1*n+j1
                    v_arr = u_arr[:]
                    v_arr[id0] = u_arr[id1]
                    v_arr[id1] = u_arr[id0]
                    v = '_'.join(v_arr)
                    if v in s2: return steps
                    if v in visited: continue
                    s.add(v)
                    visited.add(v)

            s1 = s
        return -1




        
# leetcode submit region end(Prohibit modification and deletion)
