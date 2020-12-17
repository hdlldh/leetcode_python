#
#Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
# 
#
# 
#For example, given n = 3, a solution set is:
# 
# 
#[
#  "((()))",
#  "(()())",
#  "(())()",
#  "()(())",
#  "()()()"
#]
# Related Topics String Backtracking



#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ans = []
        self.dfs(n,0,'', ans)
        return ans

    def dfs(self, n, count, out, ans):
        if count>n or count<0 or len(out)>2*n: return
        if len(out) == 2*n and count==0:
            ans.append(out)
            return
        self.dfs(n, count+1, out+'(', ans)
        self.dfs(n, count-1, out+')', ans)
        
#leetcode submit region end(Prohibit modification and deletion)
