# Let's define a function f(s) over a non-empty string s, which calculates the f
# requency of the smallest character in s. For example, if s = "dcce" then f(s) = 
# 2 because the smallest character is "c" and its frequency is 2. 
# 
#  Now, given string arrays queries and words, return an integer array answer, w
# here each answer[i] is the number of words such that f(queries[i]) < f(W), where
#  W is a word in words. 
# 
#  
#  Example 1: 
# 
#  
# Input: queries = ["cbd"], words = ["zaaaz"]
# Output: [1]
# Explanation: On the first query we have f("cbd") = 1, f("zaaaz") = 3 so f("cbd
# ") < f("zaaaz").
#  
# 
#  Example 2: 
# 
#  
# Input: queries = ["bbb","cc"], words = ["a","aa","aaa","aaaa"]
# Output: [1,2]
# Explanation: On the first query only f("bbb") < f("aaaa"). On the second query
#  both f("aaa") and f("aaaa") are both > f("cc").
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= queries.length <= 2000 
#  1 <= words.length <= 2000 
#  1 <= queries[i].length, words[i].length <= 10 
#  queries[i][j], words[i][j] are English lowercase letters. 
#  
#  Related Topics Array String


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def numSmallerByFrequency(self, queries, words):
        """
        :type queries: List[str]
        :type words: List[str]
        :rtype: List[int]
        """

        word_freq = [0] * len(words)
        for i, word in enumerate(words):
            word_freq[i] = self.getf(word)
        word_freq.sort()
        ans = [0] * len(queries)
        for i, query in enumerate(queries):
            ans[i] = self.getc(word_freq, self.getf(query))
        return ans

    def getf(self, word):
        count = collections.Counter(word)
        ch = word[0]
        f = count[ch]
        for k, v in count.items():
            if k < ch:
                ch = k
                f = count[ch]
        return f

    def getc(self, word_freq, target):
        n = len(word_freq)
        low = 0
        high = n - 1
        while low <= high:
            mid = low + (high - low) // 2
            if word_freq[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        return n - low
        
# leetcode submit region end(Prohibit modification and deletion)
