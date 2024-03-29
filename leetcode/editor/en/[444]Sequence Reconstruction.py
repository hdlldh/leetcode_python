# Check whether the original sequence org can be uniquely reconstructed from the
#  sequences in seqs. The org sequence is a permutation of the integers from 1 to 
# n, with 1 ≤ n ≤ 104. Reconstruction means building a shortest common supersequen
# ce of the sequences in seqs (i.e., a shortest sequence so that all sequences in 
# seqs are subsequences of it). Determine whether there is only one sequence that 
# can be reconstructed from seqs and it is the org sequence. 
# 
#  Example 1:
#  
# Input:
# org: [1,2,3], seqs: [[1,2],[1,3]]
# 
# Output:
# false
# 
# Explanation:
# [1,2,3] is not the only one sequence that can be reconstructed, because [1,3,2
# ] is also a valid sequence that can be reconstructed.
#  
#  
# 
#  Example 2:
#  
# Input:
# org: [1,2,3], seqs: [[1,2]]
# 
# Output:
# false
# 
# Explanation:
# The reconstructed sequence can only be [1,2].
#  
#  
# 
#  Example 3:
#  
# Input:
# org: [1,2,3], seqs: [[1,2],[1,3],[2,3]]
# 
# Output:
# true
# 
# Explanation:
# The sequences [1,2], [1,3], and [2,3] can uniquely reconstruct the original se
# quence [1,2,3].
#  
#  
# 
#  Example 4:
#  
# Input:
# org: [4,1,5,2,6,3], seqs: [[5,2,6,3],[4,1,5,2]]
# 
# Output:
# true
#  
#  
# 
#  
# UPDATE (2017/1/8): 
# The seqs parameter had been changed to a list of list of strings (instead of a
#  2d array of strings). Please reload the code definition to get the latest chang
# es.
#  Related Topics Graph Topological Sort


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def sequenceReconstruction(self, org, seqs):
        """
        :type org: List[int]
        :type seqs: List[List[int]]
        :rtype: bool
        """
        if not seqs or not org: return False
        N = len(org)
        inDegree = collections.defaultdict(int)
        outEdges = collections.defaultdict(set)
        for seq in seqs:
            if seq:
                if seq[0] not in inDegree:
                    inDegree[seq[0]] = 0
                if seq[0] > N or seq[0] < 1: return False
                for i in range(1, len(seq)):
                    u = seq[i - 1]
                    v = seq[i]
                    if v > N or v < 1: return False
                    if v in outEdges[u]: continue
                    inDegree[v] += 1
                    outEdges[u].add(v)

        queue = collections.deque()
        for u in org:
            if u not in inDegree: return False
            if inDegree[u] == 0: queue.append(u)

        ans = []
        while queue:
            if len(queue) > 1: return False
            u = queue.popleft()
            ans.append(u)
            for v in outEdges[u]:
                inDegree[v] -= 1
                if inDegree[v] == 0:
                    queue.append(v)
        # print(ans)
        return ans == org
# leetcode submit region end(Prohibit modification and deletion)
