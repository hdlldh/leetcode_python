#Given a balanced parentheses string S, compute the score of the string based on
# the following rule: 
#
# 
# () has score 1 
# AB has score A + B, where A and B are balanced parentheses strings. 
# (A) has score 2 * A, where A is a balanced parentheses string. 
# 
#
# 
#
# 
# Example 1: 
#
# 
#Input: "()"
#Output: 1
# 
#
# 
# Example 2: 
#
# 
#Input: "(())"
#Output: 2
# 
#
# 
# Example 3: 
#
# 
#Input: "()()"
#Output: 2
# 
#
# 
# Example 4: 
#
# 
#Input: "(()(()))"
#Output: 6
# 
#
# 
#
# Note: 
#
# 
# S is a balanced parentheses string, containing only ( and ). 
# 2 <= S.length <= 50 
# 
# 
# 
# 
# 
# Related Topics String Stack




#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def scoreOfParentheses(self, S):
        """
        :type S: str
        :rtype: int
        """
        n = len(S)
        if n==0: return 0
        return self.scores(S, 0, len(S)-1)

    def scores(self, S, l, r):
        if r-l==1: return 1
        b = 0
        for i in range(l, r):
            if S[i]=='(': b+=1
            else: b-=1
            if b==0: return self.scores(S,l,i) + self.scores(S, i+1, r)
        return self.scores(S, l+1, r-1)*2

#leetcode submit region end(Prohibit modification and deletion)
