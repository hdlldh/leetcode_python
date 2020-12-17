# 
# Given a set of keywords words and a string S, make all appearances of all keyw
# ords in S bold. Any letters between <b> and </b> tags become bold.
#  
# The returned string should use the least number of tags possible, and of cours
# e the tags should form a valid combination.
#  
#  
# For example, given that words = ["ab", "bc"] and S = "aabcd", we should return
#  "a<b>abc</b>d". Note that returning "a<b>a<b>b</b>c</b>d" would use more tags, 
# so it is incorrect.
#  
# 
#  Note: 
#  words has length in range [0, 50]. 
#  words[i] has length in range [1, 10]. 
#  S has length in range [0, 500]. 
#  All characters in words[i] and S are lowercase letters. 
#  Related Topics String


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def boldWords(self, words, S):
        """
        :type words: List[str]
        :type S: str
        :rtype: str
        """
        N = len(S)
        mask = [False] * N
        for i in range(N):
            prefix = S[i:]
            for word in words:
                if prefix.startswith(word):
                    for j in range(i, i+len(word)):
                        mask[j] = True
        ans = []
        for i, ch in enumerate(S):
            if mask[i] and (i==0 or not mask[i-1]): ans.append('<b>')
            ans.append(ch)
            if mask[i] and (i==N-1 or not mask[i+1]): ans.append('</b>')
        return ''.join(ans)


        
# leetcode submit region end(Prohibit modification and deletion)
