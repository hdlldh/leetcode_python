# You are given the number of rows n_rows and number of columns n_cols of a 2D b
# inary matrix where all values are initially 0. Write a function flip which choos
# es a 0 value uniformly at random, changes it to 1, and then returns the position
#  [row.id, col.id] of that value. Also, write a function reset which sets all val
# ues back to 0. Try to minimize the number of calls to system's Math.random() and
#  optimize the time and space complexity. 
# 
#  Note: 
# 
#  
#  1 <= n_rows, n_cols <= 10000 
#  0 <= row.id < n_rows and 0 <= col.id < n_cols 
#  flip will not be called when the matrix has no 0 values left. 
#  the total number of calls to flip and reset will not exceed 1000. 
#  
# 
#  Example 1: 
# 
#  
# Input: 
# ["Solution","flip","flip","flip","flip"]
# [[2,3],[],[],[],[]]
# Output: [null,[0,1],[1,2],[1,0],[1,1]]
#  
# 
#  
#  Example 2: 
# 
#  
# Input: 
# ["Solution","flip","flip","reset","flip"]
# [[1,2],[],[],[],[]]
# Output: [null,[0,0],[0,1],null,[0,0]] 
#  
# 
#  Explanation of Input Syntax: 
# 
#  The input is two lists: the subroutines called and their arguments. Solution'
# s constructor has two arguments, n_rows and n_cols. flip and reset have no argum
# ents. Arguments are always wrapped with a list, even if there aren't any. 
#  Related Topics Random


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):

    def __init__(self, n_rows, n_cols):
        """
        :type n_rows: int
        :type n_cols: int
        """
        self.n_rows = n_rows
        self.n_cols = n_cols
        self.size = n_rows * n_cols
        self.mem = {}

    def flip(self):
        """
        :rtype: List[int]
        """
        id = random.randrange(self.size)
        self.size -= 1
        val = id
        if id in self.mem: id = self.mem[id]
        if self.size in self.mem:
            self.mem[val] = self.mem[self.size]
        else:
            self.mem[val] = self.size
        return [id//self.n_cols, id%self.n_cols]
        

    def reset(self):
        """
        :rtype: None
        """
        self.size = self.n_rows * self.n_cols
        self.mem.clear()
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(n_rows, n_cols)
# param_1 = obj.flip()
# obj.reset()
# leetcode submit region end(Prohibit modification and deletion)
