# Given an array A (index starts at 1) consisting of N integers: A1, A2, ..., AN
#  and an integer B. The integer B denotes that from any place (suppose the index 
# is i) in the array A, you can jump to any one of the place in the array A indexe
# d i+1, i+2, …, i+B if this place can be jumped to. Also, if you step on the inde
# x i, you have to pay Ai coins. If Ai is -1, it means you can’t jump to the place
#  indexed i in the array. 
# 
#  Now, you start from the place indexed 1 in the array A, and your aim is to re
# ach the place indexed N using the minimum coins. You need to return the path of 
# indexes (starting from 1 to N) in the array you should take to get to the place 
# indexed N using minimum coins. 
# 
#  If there are multiple paths with the same cost, return the lexicographically 
# smallest such path. 
# 
#  If it's not possible to reach the place indexed N then you need to return an 
# empty array. 
# 
#  Example 1: 
# 
#  
# Input: [1,2,4,-1,2], 2
# Output: [1,3,5]
#  
# 
#  
# 
#  Example 2: 
# 
#  
# Input: [1,2,4,-1,2], 1
# Output: []
#  
# 
#  
# 
#  Note: 
# 
#  
#  Path Pa1, Pa2, ..., Pan is lexicographically smaller than Pb1, Pb2, ..., Pbm,
#  if and only if at the first i where Pai and Pbi differ, Pai < Pbi; when no such
#  i exists, then n < m. 
#  A1 >= 0. A2, ..., AN (if exist) will in the range of [-1, 100]. 
#  Length of A is in the range of [1, 1000]. 
#  B is in the range of [1, 100]. 
#  
# 
#  
#  Related Topics Dynamic Programming


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def cheapestJump(self, A, B):
        """
        :type A: List[int]
        :type B: int
        :rtype: List[int]
        """
        n = len(A)
        next = [-1]*n
        mem = [-1]*n
        self.jump(A, B, 0, next, mem)
        #print(next, mem)
        i = 0
        ans = []
        while i>=0 and A[i]>=0 and next[i]!=i:
            ans.append(i+1)
            i = next[i]
        if next[i] ==i and i==n-1:
            ans.append(i+1)
            return ans
        return []

    def jump(self, A, B, i, next, mem):
        if i == len(A)-1 and A[i]>=0:
            next[i] = i
            mem[i] = A[i]
            return A[i]
        if mem[i]>0: return mem[i]
        min_cost = float('inf')
        for j in range(i+1, min(len(A), i+B+1)):
            if A[i]<0: continue
            cost = A[i] + self.jump(A, B, j, next, mem)
            if cost < min_cost:
                min_cost = cost
                next[i] = j
        mem[i] = min_cost
        return min_cost
# leetcode submit region end(Prohibit modification and deletion)
