#Given two sentences words1, words2 (each represented as an array of strings), and a list of similar word pairs pairs, determine if two sentences are similar. 
#
# For example, "great acting skills" and "fine drama talent" are similar, if the similar word pairs are pairs = [["great", "fine"], ["acting","drama"], ["skills","talent"]]. 
#
# Note that the similarity relation is not transitive. For example, if "great" and "fine" are similar, and "fine" and "good" are similar, "great" and "good" are not necessarily similar. 
#
# However, similarity is symmetric. For example, "great" and "fine" being similar is the same as "fine" and "great" being similar. 
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
# Related Topics Hash Table



#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def areSentencesSimilar(self, words1, words2, pairs):
        """
        :type words1: List[str]
        :type words2: List[str]
        :type pairs: List[List[str]]
        :rtype: bool
        """
        n1 = len(words1)
        n2 = len(words2)
        if n1!=n2: return False
        hmap = collections.defaultdict(set)
        for word1, word2 in pairs:
            hmap[word1].add(word2)
            hmap[word2].add(word1)
        for i in range(n1):
            if words1[i] == words2[i]: continue
            if words1[i] not in hmap or words2[i] not in hmap[words1[i]]: return False
        return True
        
#leetcode submit region end(Prohibit modification and deletion)
