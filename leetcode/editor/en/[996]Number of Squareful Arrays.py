#Given an array A of non-negative integers, the array is squareful if for every pair of adjacent elements, their sum is a perfect square. 
#
# Return the number of permutations of A that are squareful. Two permutations A1 and A2 differ if and only if there is some index i such that A1[i] != A2[i]. 
#
# 
#
# Example 1: 
#
# 
#Input: [1,17,8]
#Output: 2
#Explanation: 
#[1,8,17] and [17,8,1] are the valid permutations.
# 
#
# Example 2: 
#
# 
#Input: [2,2,2]
#Output: 1
# 
#
# 
#
# Note: 
#
# 
# 1 <= A.length <= 12 
# 0 <= A[i] <= 1e9 
# Related Topics Math Backtracking Graph



#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def numSquarefulPerms(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if not A: return 0
        A.sort()
        n = len(A)
        visited = [0]*n
        ans = []
        def isSqure(x, y):
            low = 0
            high = x+y
            while low<=high:
                mid = low+(high-low)//2
                mid2 = mid*mid
                if mid2>x+y: high = mid -1
                elif mid2<x+y: low = mid+1
                else: return True
            return False

        def dfs(A, out, ans, visited):
            if len(out)==len(A):
                ans.append(out)
                return
            for i, num in enumerate(A):
                if visited[i]==1: continue
                if i==0 or num != A[i-1] or visited[i-1]==1:
                    if not out or isSqure(out[-1],A[i]):
                        visited[i] = 1
                        dfs(A, out+[A[i]], ans, visited)
                        visited[i] = 0

        dfs(A, [], ans, visited)
        return len(ans)
#leetcode submit region end(Prohibit modification and deletion)
