#In a social group, there are N people, with unique integer ids from 0 to N-1. 
#
# We have a list of logs, where each logs[i] = [timestamp, id_A, id_B] contains 
#a non-negative integer timestamp, and the ids of two different people. 
#
# Each log represents the time in which two different people became friends. Fri
#endship is symmetric: if A is friends with B, then B is friends with A. 
#
# Let's say that person A is acquainted with person B if A is friends with B, or
# A is a friend of someone acquainted with B. 
#
# Return the earliest time for which every person became acquainted with every o
#ther person. Return -1 if there is no such earliest time. 
#
# 
#
# Example 1: 
#
# 
#Input: logs = [[20190101,0,1],[20190104,3,4],[20190107,2,3],[20190211,1,5],[201
#90224,2,4],[20190301,0,3],[20190312,1,2],[20190322,4,5]], N = 6
#Output: 20190301
#Explanation: 
#The first event occurs at timestamp = 20190101 and after 0 and 1 become friends
# we have the following friendship groups [0,1], [2], [3], [4], [5].
#The second event occurs at timestamp = 20190104 and after 3 and 4 become friend
#s we have the following friendship groups [0,1], [2], [3,4], [5].
#The third event occurs at timestamp = 20190107 and after 2 and 3 become friends
# we have the following friendship groups [0,1], [2,3,4], [5].
#The fourth event occurs at timestamp = 20190211 and after 1 and 5 become friend
#s we have the following friendship groups [0,1,5], [2,3,4].
#The fifth event occurs at timestamp = 20190224 and as 2 and 4 are already frien
#d anything happens.
#The sixth event occurs at timestamp = 20190301 and after 0 and 3 become friends
# we have that all become friends.
# 
#
# 
#
# Note: 
#
# 
# 2 <= N <= 100 
# 1 <= logs.length <= 10^4 
# 0 <= logs[i][0] <= 10^9 
# 0 <= logs[i][1], logs[i][2] <= N - 1 
# It's guaranteed that all timestamps in logs[i][0] are different. 
# logs are not necessarily ordered by some criteria. 
# logs[i][1] != logs[i][2] 
# 
# Related Topics Union Find




#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def earliestAcq(self, logs, N):
        """
        :type logs: List[List[int]]
        :type N: int
        :rtype: int
        """
        logs.sort()
        roots = [i for i in range(N)]
        size = [1] * N
        for t, u, v in logs:
            if self.union(roots, u, v, size): return t
        return -1

    def find(self, roots, i):
        while i != roots[i]: i=roots[i]
        return i

    def union(self, roots, i, j, size):
        roots_i = self.find(roots, i)
        roots_j = self.find(roots, j)
        if roots_i!=roots_j:
            roots[roots_j] = roots_i
            size[roots_i] += size[roots_j]
            if size[roots_i] == len(roots): return True
        return False
        
#leetcode submit region end(Prohibit modification and deletion)
