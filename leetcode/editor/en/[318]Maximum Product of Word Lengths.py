#Given a string array words, find the maximum value of length(word[i]) * length(word[j]) where the two words do not share common letters. You may assume that each word will contain only lower case letters. If no such two words exist, return 0. 
#
# Example 1: 
#
# 
#Input: ["abcw","baz","foo","bar","xtfn","abcdef"]
#Output: 16 
#Explanation: The two words can be "abcw", "xtfn". 
#
# Example 2: 
#
# 
#Input: ["a","ab","abc","d","cd","bcd","abcd"]
#Output: 4 
#Explanation: The two words can be "ab", "cd". 
#
# Example 3: 
#
# 
#Input: ["a","aa","aaa","aaaa"]
#Output: 0 
#Explanation: No such pair of words.
# 
# Related Topics Bit Manipulation



#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        n = len(words)
        mask = [0] * n
        ans = 0
        for i, word in enumerate(words):
            for ch in word:
                mask[i] |= 1<<(ord(ch)-ord('a'))
            for j in range(i):
                if (mask[i] & mask[j])==0:
                    ans = max(ans, len(words[i])*len(words[j]))
        return ans
#leetcode submit region end(Prohibit modification and deletion)
