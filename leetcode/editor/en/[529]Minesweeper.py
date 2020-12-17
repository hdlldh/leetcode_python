#Let's play the minesweeper game (Wikipedia, online game)! 
#
# You are given a 2D char matrix representing the game board. 'M' represents an 
#unrevealed mine, 'E' represents an unrevealed empty square, 'B' represents a rev
#ealed blank square that has no adjacent (above, below, left, right, and all 4 di
#agonals) mines, digit ('1' to '8') represents how many mines are adjacent to thi
#s revealed square, and finally 'X' represents a revealed mine. 
#
# Now given the next click position (row and column indices) among all the unrev
#ealed squares ('M' or 'E'), return the board after revealing this position accor
#ding to the following rules: 
#
# 
# If a mine ('M') is revealed, then the game is over - change it to 'X'. 
# If an empty square ('E') with no adjacent mines is revealed, then change it to
# revealed blank ('B') and all of its adjacent unrevealed squares should be revea
#led recursively. 
# If an empty square ('E') with at least one adjacent mine is revealed, then cha
#nge it to a digit ('1' to '8') representing the number of adjacent mines. 
# Return the board when no more squares will be revealed. 
# 
#
# 
#
# Example 1: 
#
# 
#Input: 
#
#[['E', 'E', 'E', 'E', 'E'],
# ['E', 'E', 'M', 'E', 'E'],
# ['E', 'E', 'E', 'E', 'E'],
# ['E', 'E', 'E', 'E', 'E']]
#
#Click : [3,0]
#
#Output: 
#
#[['B', '1', 'E', '1', 'B'],
# ['B', '1', 'M', '1', 'B'],
# ['B', '1', '1', '1', 'B'],
# ['B', 'B', 'B', 'B', 'B']]
#
#Explanation:
#
# 
#
# Example 2: 
#
# 
#Input: 
#
#[['B', '1', 'E', '1', 'B'],
# ['B', '1', 'M', '1', 'B'],
# ['B', '1', '1', '1', 'B'],
# ['B', 'B', 'B', 'B', 'B']]
#
#Click : [1,2]
#
#Output: 
#
#[['B', '1', 'E', '1', 'B'],
# ['B', '1', 'X', '1', 'B'],
# ['B', '1', '1', '1', 'B'],
# ['B', 'B', 'B', 'B', 'B']]
#
#Explanation:
#
# 
#
# 
#
# Note: 
#
# 
# The range of the input matrix's height and width is [1,50]. 
# The click position will only be an unrevealed square ('M' or 'E'), which also 
#means the input board contains at least one clickable square. 
# The input board won't be a stage when game is over (some mines have been revea
#led). 
# For simplicity, not mentioned rules should be ignored in this problem. For exa
#mple, you don't need to reveal all the unrevealed mines when the game is over, c
#onsider any cases that you will win the game or flag any squares. 
# 
# Related Topics Depth-first Search Breadth-first Search




#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """
        m, n = len(board), len(board[0])
        x, y = click[0], click[1]

        if board[x][y] == 'M':
            board[x][y] = 'X'
        else:
            cnt = 0
            for dx in range(-1,2):
                for dy in range(-1, 2):
                    if dx==dy==0: continue
                    tx = x+dx
                    ty = y+dy
                    if tx<0 or tx>=m or ty<0 or ty>=n: continue
                    if board[tx][ty] == 'M': cnt+=1
            if cnt>0: board[x][y] = str(cnt)
            else:
                board[x][y] = 'B'
                for dx in range(-1, 2):
                    for dy in range(-1, 2):
                        if dx == dy == 0: continue
                        tx = x + dx
                        ty = y + dy
                        if tx < 0 or tx >= m or ty < 0 or ty >= n: continue
                        if board[tx][ty] == 'E': self.updateBoard(board, [tx, ty])
        return board


        
#leetcode submit region end(Prohibit modification and deletion)
