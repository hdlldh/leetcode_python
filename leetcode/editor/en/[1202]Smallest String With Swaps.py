# You are given a string s, and an array of pairs of indices in the string pairs
#  where pairs[i] = [a, b] indicates 2 indices(0-indexed) of the string. 
# 
#  You can swap the characters at any pair of indices in the given pairs any num
# ber of times. 
# 
#  Return the lexicographically smallest string that s can be changed to after u
# sing the swaps. 
# 
#  
#  Example 1: 
# 
#  
# Input: s = "dcab", pairs = [[0,3],[1,2]]
# Output: "bacd"
# Explaination: 
# Swap s[0] and s[3], s = "bcad"
# Swap s[1] and s[2], s = "bacd"
#  
# 
#  Example 2: 
# 
#  
# Input: s = "dcab", pairs = [[0,3],[1,2],[0,2]]
# Output: "abcd"
# Explaination: 
# Swap s[0] and s[3], s = "bcad"
# Swap s[0] and s[2], s = "acbd"
# Swap s[1] and s[2], s = "abcd" 
# 
#  Example 3: 
# 
#  
# Input: s = "cba", pairs = [[0,1],[1,2]]
# Output: "abc"
# Explaination: 
# Swap s[0] and s[1], s = "bca"
# Swap s[1] and s[2], s = "bac"
# Swap s[0] and s[1], s = "abc"
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= s.length <= 10^5 
#  0 <= pairs.length <= 10^5 
#  0 <= pairs[i][0], pairs[i][1] < s.length 
#  s only contains lower case English letters. 
#  
#  Related Topics Array Union Find


# leetcode submit region begin(Prohibit modification and deletion)
class union_find(object):
    def __init__(self, n):
        self.parents = [i for i in range(n)]

    def find(self, i):
        if self.parents[i] == i: return i
        self.parents[i] = self.find(self.parents[i])
        return self.parents[i]

    def union(self, i, j):
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i != root_j:
            self.parents[root_j] = root_i


class Solution(object):
    def smallestStringWithSwaps(self, s, pairs):
        """
        :type s: str
        :type pairs: List[List[int]]
        :rtype: str
        """
        n = len(s)
        graph = union_find(n)
        for p1, p2 in pairs:
            graph.union(p1, p2)

        data = {}
        for i, ch in enumerate(s):
            root_i = graph.find(i)
            if root_i not in data:
                data[root_i] = [ch]
            else:
                data[root_i].append(ch)

        for k in data.keys(): data[k].sort()

        ans = [''] * n
        for i, ch in enumerate(s):
            root_i = graph.find(i)
            ans[i] = data[root_i][0]
            data[root_i].pop(0)
        return ''.join(ans)
        
# leetcode submit region end(Prohibit modification and deletion)
