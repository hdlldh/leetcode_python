#Given two sentences words1, words2 (each represented as an array of strings), and a list of similar word pairs pairs, determine if two sentences are similar. 
#
# For example, words1 = ["great", "acting", "skills"] and words2 = ["fine", "drama", "talent"] are similar, if the similar word pairs are pairs = [["great", "good"], ["fine", "good"], ["acting","drama"], ["skills","talent"]]. 
#
# Note that the similarity relation is transitive. For example, if "great" and "good" are similar, and "fine" and "good" are similar, then "great" and "fine" are similar. 
#
# Similarity is also symmetric. For example, "great" and "fine" being similar is the same as "fine" and "great" being similar. 
#
# Also, a word is always similar with itself. For example, the sentences words1 = ["great"], words2 = ["great"], pairs = [] are similar, even though there are no specified similar word pairs. 
#
# Finally, sentences can only be similar if they have the same number of words. So a sentence like words1 = ["great"] can never be similar to words2 = ["doubleplus","good"]. 
#
# Note: 
#
# 
# The length of words1 and words2 will not exceed 1000. 
# The length of pairs will not exceed 2000. 
# The length of each pairs[i] will be 2. 
# The length of each words[i] and pairs[i][j] will be in the range [1, 20]. 
# 
#
# 
# Related Topics Depth-first Search Union Find



#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def areSentencesSimilarTwo(self, words1, words2, pairs):
        """
        :type words1: List[str]
        :type words2: List[str]
        :type pairs: List[List[str]]
        :rtype: bool
        """
        n1 = len(words1)
        n2 = len(words2)
        if n1!=n2: return False
        index = {}
        for p, q in pairs:
            if p not in index: index[p] = len(index)
            if q not in index: index[q] = len(index)

        roots = [i for i in range(len(index))]
        for p, q in pairs:
            pi = index[p]
            qi = index[q]
            self.union(roots, pi, qi)

        for i in range(n1):
            word1 = words1[i]
            word2 = words2[i]
            if word1== word2: continue
            if word1 not in index or word2 not in index: return False
            if self.find(roots, index[word1]) != self.find(roots, index[word2]): return False
        return True

    def find(self, roots, p):
        while p!=roots[p]: p = roots[p]
        return p

    def union(self, roots, p, q):
        root_p = self.find(roots, p)
        root_q = self.find(roots, q)
        roots[root_q] = root_p
        
#leetcode submit region end(Prohibit modification and deletion)
