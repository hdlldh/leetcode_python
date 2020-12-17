# Given a picture consisting of black and white pixels, find the number of black
#  lonely pixels. 
# 
#  The picture is represented by a 2D char array consisting of 'B' and 'W', whic
# h means black and white pixels respectively. 
# 
#  A black lonely pixel is character 'B' that located at a specific position whe
# re the same row and same column don't have any other black pixels. 
# 
#  Example: 
#  
# Input: 
# [['W', 'W', 'B'],
#  ['W', 'B', 'W'],
#  ['B', 'W', 'W']]
# 
# Output: 3
# Explanation: All the three 'B's are black lonely pixels.
#  
#  
# 
#  Note: 
#  
#  The range of width and height of the input 2D array is [1,500]. 
#  
#  Related Topics Array Depth-first Search


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def findLonelyPixel(self, picture):
        """
        :type picture: List[List[str]]
        :rtype: int
        """
        m, n = len(picture), len(picture[0])
        rowCnt = [0] * n
        colCnt = [0] * m
        for i in range(m):
            for j in range(n):
                if picture[i][j] == 'B':
                    rowCnt[j] += 1
                    colCnt[i] += 1

        ans = 0
        for i in range(m):
            for j in range(n):
                if picture[i][j]=='B' and rowCnt[j]==1 and colCnt[i]==1:
                    ans +=1
        return ans
# leetcode submit region end(Prohibit modification and deletion)
