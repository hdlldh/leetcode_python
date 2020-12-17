#There is a new alien language which uses the latin alphabet. However, the order among letters are unknown to you. You receive a list of non-empty words from the dictionary, where words are sorted lexicographically by the rules of this new language. Derive the order of letters in this language. 
#
# Example 1: 
#
# 
#Input:
#[
#  "wrt",
#  "wrf",
#  "er",
#  "ett",
#  "rftt"
#]
#
#Output: "wertf"
# 
#
# Example 2: 
#
# 
#Input:
#[
#  "z",
#  "x"
#]
#
#Output: "zx"
# 
#
# Example 3: 
#
# 
#Input:
#[
#  "z",
#  "x",
#  "z"
#] 
#
#Output: "" 
#
#Explanation: The order is invalid, so return "".
# 
#
# Note: 
#
# 
# You may assume all letters are in lowercase. 
# You may assume that if a is a prefix of b, then a must appear before b in the given dictionary. 
# If the order is invalid, return an empty string. 
# There may be multiple valid order of letters, return any one of them is fine. 
# 
# Related Topics Graph Topological Sort



#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        N = len(words)
        inDegree = collections.defaultdict(int)
        outEdges = collections.defaultdict(set)
        for i in range(N):
            for j in range(i+1, N):
                w1 = words[i]
                w2 = words[j]
                l1 = len(w1)
                l2 = len(w2)
                k = 0
                while k< min(l1,l2):
                    if w1[k]!=w2[k]:break
                    k+=1
                if l1>l2 and l2==k: return ""
                if k<min(l1, l2):
                    outEdges[w1[k]].add(w2[k])


        queue = collections.deque()
        chars = set(''.join(words))
        for ch in chars: inDegree[ch] = 0
        for u in outEdges:
            for v in outEdges[u]:
                inDegree[v] += 1

        ans = []
        for u in inDegree:
            if inDegree[u]==0: queue.append(u)

        #print(outEdges, inDegree)

        while queue:
            u = queue.popleft()
            ans.append(u)
            for v in outEdges[u]:
                inDegree[v] -= 1
                if inDegree[v]==0: queue.append(v)
        ans = ''.join(ans)
        if len(ans) != len(chars): return ""
        return ''.join(ans)
        
#leetcode submit region end(Prohibit modification and deletion)
