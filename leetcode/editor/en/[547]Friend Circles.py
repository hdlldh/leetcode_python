#
#There are N students in a class. Some of them are friends, while some are not. Their friendship is transitive in nature. For example, if A is a direct friend of B, and B is a direct friend of C, then A is an indirect friend of C. And we defined a friend circle is a group of students who are direct or indirect friends.
# 
#
# 
#Given a N*N matrix M representing the friend relationship between students in the class. If M[i][j] = 1, then the ith and jth students are direct friends with each other, otherwise not. And you have to output the total number of friend circles among all the students.
# 
#
# Example 1: 
# 
#Input: 
#[[1,1,0],
# [1,1,0],
# [0,0,1]]
#Output: 2
#Explanation:The 0th and 1st students are direct friends, so they are in a friend circle. The 2nd student himself is in a friend circle. So return 2.
# 
# 
#
# Example 2: 
# 
#Input: 
#[[1,1,0],
# [1,1,1],
# [0,1,1]]
#Output: 1
#Explanation:The 0th and 1st students are direct friends, the 1st and 2nd students are direct friends, so the 0th and 2nd students are indirect friends. All of them are in the same friend circle, so return 1.
# 
# 
#
#
# Note: 
# 
# N is in range [1,200]. 
# M[i][i] = 1 for all students. 
# If M[i][j] = 1, then M[j][i] = 1. 
# 
# Related Topics Depth-first Search Union Find



#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        n = len(M)
        if n==0: return 0
        parent = [i for i in range(n)]
        for i in range(n):
            for j in range(i+1, n):
                if M[i][j] == 1: self.union(parent, i, j)
        ans = 0
        for i in range(n):
            if i == parent[i]: ans += 1
        return ans

    def find(self, parent, i):
        while i!= parent[i]: i=parent[i]
        return i

    def union(self, parent, i, j):
        root_i = self.find(parent, i)
        root_j = self.find(parent, j)
        if root_i!=root_j: parent[root_j] = root_i
        
#leetcode submit region end(Prohibit modification and deletion)
