# Your task is to design the basic function of Excel and implement the function 
# of sum formula. Specifically, you need to implement the following functions: 
# 
# 
# 
#  Excel(int H, char W): This is the constructor. The inputs represents the heig
# ht and width of the Excel form. H is a positive integer, range from 1 to 26. It 
# represents the height. W is a character range from 'A' to 'Z'. It represents tha
# t the width is the number of characters from 'A' to W. The Excel form content is
#  represented by a height * width 2D integer array C, it should be initialized to
#  zero. You should assume that the first row of C starts from 1, and the first co
# lumn of C starts from 'A'. 
# 
#  
# 
#  void Set(int row, char column, int val): Change the value at C(row, column) t
# o be val. 
#  
#  int Get(int row, char column): Return the value at C(row, column). 
#  
#  int Sum(int row, char column, List of Strings : numbers): This function calcu
# late and set the value at C(row, column), where the value should be the sum of c
# ells represented by numbers. This function return the sum result at C(row, colum
# n). This sum formula should exist until this cell is overlapped by another value
#  or another sum formula. 
# 
#  numbers is a list of strings that each string represent a cell or a range of 
# cells. If the string represent a single cell, then it has the following format :
#  ColRow. For example, "F7" represents the cell at (7, F). 
# 
#  If the string represent a range of cells, then it has the following format : 
# ColRow1:ColRow2. The range will always be a rectangle, and ColRow1 represent the
#  position of the top-left cell, and ColRow2 represents the position of the botto
# m-right cell. 
#  
#  Example 1: 
#  
# Excel(3,"C"); 
# // construct a 3*3 2D array with all zero.
# //   A B C
# // 1 0 0 0
# // 2 0 0 0
# // 3 0 0 0
# 
# Set(1, "A", 2);
# // set C(1,"A") to be 2.
# //   A B C
# // 1 2 0 0
# // 2 0 0 0
# // 3 0 0 0
# 
# Sum(3, "C", ["A1", "A1:B2"]);
# // set C(3,"C") to be the sum of value at C(1,"A") and the values sum of the r
# ectangle range whose top-left cell is C(1,"A") and bottom-right cell is C(2,"B")
# . Return 4. 
# //   A B C
# // 1 2 0 0
# // 2 0 0 0
# // 3 0 0 4
# 
# Set(2, "B", 2);
# // set C(2,"B") to be 2. Note C(3, "C") should also be changed.
# //   A B C
# // 1 2 0 0
# // 2 0 2 0
# // 3 0 0 6
#  
#  
# 
#  Note: 
#  
#  You could assume that there won't be any circular sum reference. For example,
#  A1 = sum(B1) and B1 = sum(A1). 
#  The test cases are using double-quotes to represent a character. 
#  Please remember to RESET your class variables declared in class Excel, as sta
# tic/class variables are persisted across multiple test cases. Please see here fo
# r more details. 
#  
#  Related Topics Design


# leetcode submit region begin(Prohibit modification and deletion)
class Excel(object):

    def __init__(self, H, W):
        """
        :type H: int
        :type W: str
        """
        self.mem = {}
        self.mat = [[0]*(ord(W)-ord('A')+1) for _ in range(H)]
        

    def set(self, r, c, v):
        """
        :type r: int
        :type c: str
        :type v: int
        :rtype: None
        """
        if (r, c) in self.mem: self.mem.pop((r, c))
        self.mat[r-1][ord(c)-ord('A')] = v
        

    def get(self, r, c):
        """
        :type r: int
        :type c: str
        :rtype: int
        """
        if (r, c) in self.mem: return self.sum(r, c, self.mem[(r, c)])
        return self.mat[r-1][ord(c)-ord('A')]
        

    def sum(self, r, c, strs):
        """
        :type r: int
        :type c: str
        :type strs: List[str]
        :rtype: int
        """
        ans = 0
        for s in strs:
            if ":" not in s:
                ans += self.get(int(s[1:]), s[0])
            else:
                c1, c2 = s.split(':')
                c1r, c1c = int(c1[1:]), ord(c1[0])
                c2r, c2c = int(c2[1:]), ord(c2[0])
                for i in range(c1r, c2r+1):
                    for j in range(c1c, c2c+1):
                        k = chr(j)
                        ans += self.get(i, k)
        self.mem[(r,c)] = strs
        return ans
        


# Your Excel object will be instantiated and called as such:
# obj = Excel(H, W)
# obj.set(r,c,v)
# param_2 = obj.get(r,c)
# param_3 = obj.sum(r,c,strs)
# leetcode submit region end(Prohibit modification and deletion)
