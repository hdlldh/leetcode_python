# Strings A and B are K-similar (for some non-negative integer K) if we can swap
#  the positions of two letters in A exactly K times so that the resulting string 
# equals B. 
# 
#  Given two anagrams A and B, return the smallest K for which A and B are K-sim
# ilar. 
# 
#  Example 1: 
# 
#  
# Input: A = "ab", B = "ba"
# Output: 1
#  
# 
#  
#  Example 2: 
# 
#  
# Input: A = "abc", B = "bca"
# Output: 2
#  
# 
#  
#  Example 3: 
# 
#  
# Input: A = "abac", B = "baca"
# Output: 2
#  
# 
#  
#  Example 4: 
# 
#  
# Input: A = "aabc", B = "abca"
# Output: 2 
#  
#  
#  
# 
#  Note: 
# 
#  
#  1 <= A.length == B.length <= 20 
#  A and B contain only lowercase letters from the set {'a', 'b', 'c', 'd', 'e',
#  'f'} 
#  
#  Related Topics Breadth-first Search Graph


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def kSimilarity(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        queue = collections.deque()
        queue.append(A)
        visited = set()
        visited.add(A)
        steps = 0
        n = len(A)
        while queue:
            size = len(queue)
            for _ in range(size):
                cur = queue.popleft()
                if cur == B: return steps
                i = 0
                while i<n and cur[i] == B[i]: i+=1
                for j in range(i+1,n):
                    if cur[j] == B[j] or cur[i]!=B[j]: continue
                    nxt = cur[:i]+cur[j]+cur[i+1:j]+cur[i]+cur[j+1:]
                    if nxt in visited: continue
                    queue.append(nxt)
            steps += 1
        return steps

# leetcode submit region end(Prohibit modification and deletion)
