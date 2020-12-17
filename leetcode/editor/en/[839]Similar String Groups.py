# Two strings X and Y are similar if we can swap two letters (in different posit
# ions) of X, so that it equals Y. Also two strings X and Y are similar if they ar
# e equal. 
# 
#  For example, "tars" and "rats" are similar (swapping at positions 0 and 2), a
# nd "rats" and "arts" are similar, but "star" is not similar to "tars", "rats", o
# r "arts". 
# 
#  Together, these form two connected groups by similarity: {"tars", "rats", "ar
# ts"} and {"star"}. Notice that "tars" and "arts" are in the same group even thou
# gh they are not similar. Formally, each group is such that a word is in the grou
# p if and only if it is similar to at least one other word in the group. 
# 
#  We are given a list A of strings. Every string in A is an anagram of every ot
# her string in A. How many groups are there? 
# 
#  
#  Example 1: 
#  Input: A = ["tars","rats","arts","star"]
# Output: 2
#  
#  
#  Constraints: 
# 
#  
#  1 <= A.length <= 2000 
#  1 <= A[i].length <= 1000 
#  A.length * A[i].length <= 20000 
#  All words in A consist of lowercase letters only. 
#  All words in A have the same length and are anagrams of each other. 
#  The judging time limit has been increased for this question. 
#  
#  Related Topics Depth-first Search Union Find Graph


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def numSimilarGroups(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        N = len(A)
        if N == 0: return 0
        W = len(A[0])
        wordset = set(A)
        B = list(wordset)
        N = len(B)

        parents = [i for i in range(N)]

        def find(parents, i):
            while i != parents[i]: i = parents[i]
            return i

        def union(parents, i, j):
            root_i = find(parents, i)
            root_j = find(parents, j)
            if root_i != root_j:
                parents[root_j] = root_i

        def num_roots(parents):
            ans = 0
            for i in range(len(parents)):
                if parents[i] == i: ans += 1
            return ans

        def is_similar(w1, w2):
            ans = 0
            for i in range(len(w1)):
                if w1[i] != w2[i]: ans += 1
            return ans == 2

        if N < W:
            for i in range(N):
                for j in range(i + 1, N):
                    if i == j: continue
                    if is_similar(B[i], B[j]): union(parents, i, j)
            return num_roots(parents)
        else:
            worddict = {}
            for i, w in enumerate(B): worddict[w] = i
            for i, w in enumerate(B):
                for l in range(W):
                    for r in range(l + 1, W):
                        if w[l] == w[r]: continue
                        w2 = w[:l] + w[r] + w[l + 1:r] + w[l] + w[r + 1:]
                        if w2 in wordset:
                            union(parents, i, worddict[w2])

            return num_roots(parents)
        
# leetcode submit region end(Prohibit modification and deletion)
