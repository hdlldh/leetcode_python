# Given several boxes with different colors represented by different positive nu
# mbers. 
# You may experience several rounds to remove boxes until there is no box left. 
# Each time you can choose some continuous boxes with the same color (composed of 
# k boxes, k >= 1), remove them and get k*k points. 
# Find the maximum points you can get.
#  
# 
#  Example 1: 
# Input: 
#  
# [1, 3, 2, 2, 2, 3, 4, 3, 1]
#  
# Output:
#  
# 23
#  
# Explanation: 
#  
# [1, 3, 2, 2, 2, 3, 4, 3, 1] 
# ----> [1, 3, 3, 4, 3, 1] (3*3=9 points) 
# ----> [1, 3, 3, 3, 1] (1*1=1 points) 
# ----> [1, 1] (3*3=9 points) 
# ----> [] (2*2=4 points)
#  
#  
# 
#  Note:
# The number of boxes n would not exceed 100.
#  
#  Related Topics Dynamic Programming Depth-first Search


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def removeBoxes(self, boxes):
        """
        :type boxes: List[int]
        :rtype: int
        """
        n = len(boxes)
        mem = [[[0 for _ in range(n)] for _ in range(n)] for _ in range(n)]
        return self.helper(boxes, 0, n-1, 0, mem)

    def helper(self, boxes, l, r, k, mem):
        if l>r: return 0
        if mem[l][r][k]>0: return mem[l][r][k]
        mem[l][r][k] = self.helper(boxes, l, r-1, 0, mem) + (k+1)**2
        for i in range(l, r):
            if boxes[i]==boxes[r]:
                mem[l][r][k] = max(mem[l][r][k], self.helper(boxes, l, i, k+1, mem) + self.helper(boxes, i+1, r-1, 0, mem))
        return mem[l][r][k]


        
# leetcode submit region end(Prohibit modification and deletion)
