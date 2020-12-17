# Two images A and B are given, represented as binary, square matrices of the sa
# me size. (A binary matrix has only 0s and 1s as values.) 
# 
#  We translate one image however we choose (sliding it left, right, up, or down
#  any number of units), and place it on top of the other image. After, the overla
# p of this translation is the number of positions that have a 1 in both images. 
# 
#  (Note also that a translation does not include any kind of rotation.) 
# 
#  What is the largest possible overlap? 
# 
#  Example 1: 
# 
#  
# Input: A = [[1,1,0],
#             [0,1,0],
#             [0,1,0]]
#        B = [[0,0,0],
#             [0,1,1],
#             [0,0,1]]
# Output: 3
# Explanation: We slide A to right by 1 unit and down by 1 unit. 
# 
#  Notes: 
# 
#  
#  1 <= A.length = A[0].length = B.length = B[0].length <= 30 
#  0 <= A[i][j], B[i][j] <= 1 
#  
#  Related Topics Array


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def largestOverlap(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: int
        """
        n = len(A)
        listA = []
        listB = []
        for i in range(n):
            for j in range(n):
                if A[i][j] == 1: listA.append((i, j))
                if B[i][j] == 1: listB.append((i, j))

        ans = 0
        count = collections.defaultdict(int)
        for i1, j1 in listA:
            for i2, j2 in listB:
                signature = '%s_%s'%(i1-i2, j1-j2)
                count[signature] += 1
                ans = max(ans, count[signature])
        return ans


# leetcode submit region end(Prohibit modification and deletion)
