#Given an array A of strings, find any smallest string that contains each string
# in A as a substring. 
#
# We may assume that no string in A is substring of another string in A. 
#
# 
#
# 
# Example 1: 
#
# 
#Input: ["alex","loves","leetcode"]
#Output: "alexlovesleetcode"
#Explanation: All permutations of "alex","loves","leetcode" would also be accept
#ed.
# 
#
# 
# Example 2: 
#
# 
#Input: ["catg","ctaagt","gcta","ttca","atgcatc"]
#Output: "gctaagttcatgcatc" 
#
# 
# 
# 
#
# Note: 
#
# 
# 1 <= A.length <= 12 
# 1 <= A[i].length <= 20 
# 
#
# 
# 
# Related Topics Dynamic Programming




#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def shortestSuperstring(self, A):
        """
        :type A: List[str]
        :rtype: str
        """

        def get_distance(s1, s2):
            l = 0
            for i in range(1, min(len(s1), len(s2))):
                if s1[-i:] == s2[:i]: l = max(l, i)
            return l
        n =len(A)
        G = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(i+1, n):
                G[i][j] = get_distance(A[i],A[j])
                G[j][i] = get_distance(A[j],A[i])

        status = [[0]*n for _ in range(1<<n)]
        queue = collections.deque([(i, 1<<i, [i], 0) for i in range(n)])
        max_len = -1
        max_path = []
        while queue:
            u, mask, path, dis = queue.popleft()
            if dis < status[mask][u]: continue
            if mask == (1<<n) - 1 and dis > max_len:
                max_path = path
                max_len = dis
                continue
            for v in range(n):
                next_mask = mask | (1<<v)
                if next_mask != mask and status[mask][u] + G[u][v] >= status[next_mask][v]:
                    status[next_mask][v] = status[mask][u] + G[u][v]
                    queue.append((v, next_mask, path+[v], status[next_mask][v]))

        ans = A[max_path[0]]
        for i in range(1, len(max_path)):
            d = G[max_path[i-1]][max_path[i]]
            ans += A[max_path[i]][d:]
        return ans


        
#leetcode submit region end(Prohibit modification and deletion)
