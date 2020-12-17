#Given a matrix of M x N elements (M rows, N columns), return all elements of th
#e matrix in diagonal order as shown in the below image. 
#
# 
#
# Example: 
#
# 
#Input:
#[
# [ 1, 2, 3 ],
# [ 4, 5, 6 ],
# [ 7, 8, 9 ]
#]
#
#Output:  [1,2,4,7,5,3,6,8,9]
#
#Explanation:
#
# 
#
# 
#
# Note: 
#
# The total number of elements of the given matrix will not exceed 10,000. 
#




#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        ans = []
        m = len(matrix)
        if m==0: return ans
        n = len(matrix[0])
        dir = 1
        for k in range(n):
            t = []
            i = 0
            j = k
            while i>=0 and i<m and j>=0 and j<n:
                t.append(matrix[i][j])
                i+=1
                j-=1
            if dir==1: t.reverse()
            ans.extend(t)
            dir = -dir
        for k in range(1, m):
            t = []
            i=k;
            j=n-1;
            while i>=0 and i<m and j>=0 and j<n:
                t.append(matrix[i][j])
                i+=1
                j-=1
            if dir == 1: t.reverse()
            ans.extend(t)
            dir = -dir
        return ans

        
#leetcode submit region end(Prohibit modification and deletion)
