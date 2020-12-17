#Given string S and a dictionary of words words, find the number of words[i] that is a subsequence of S. 
#
# 
#Example :
#Input: 
#S = "abcde"
#words = ["a", "bb", "acd", "ace"]
#Output: 3
#Explanation: There are three words in words that are a subsequence of S: "a", "acd", "ace".
# 
#
# Note: 
#
# 
# All words in words and S will only consists of lowercase letters. 
# The length of S will be in the range of [1, 50000]. 
# The length of words will be in the range of [1, 5000]. 
# The length of words[i] will be in the range of [1, 50]. 
# 
# Related Topics Array

import bisect

#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def numMatchingSubseq(self, S, words):
        """
        :type S: str
        :type words: List[str]
        :rtype: int
        """
        mem = collections.defaultdict(list)
        for i, ch in enumerate(S): mem[ch].append(i)
        ans =0
        for word in words:
            prev = -1
            for i in range(len(word)):
                if word[i] not in mem: break
                pos = bisect.bisect_left(mem[word[i]], prev+1)
                if pos == len(mem[word[i]]): break
                prev = mem[word[i]][pos]
                if i==len(word)-1: ans+= 1
        return ans
#leetcode submit region end(Prohibit modification and deletion)
