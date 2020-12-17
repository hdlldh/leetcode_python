#Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. 
#
# A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters. 
#
# 
#
# Example: 
#
# 
#Input: "23"
#Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
# 
#
# Note: 
#
# Although the above answer is in lexicographical order, your answer could be in any order you want. 
# Related Topics String Backtracking



#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits: return []
        mem = {}
        mem['2'] = 'abc'
        mem['3'] = 'def'
        mem['4'] = 'ghi'
        mem['5'] = 'jkl'
        mem['6'] = 'mno'
        mem['7'] = 'pqrs'
        mem['8'] = 'tuv'
        mem['9'] = 'wxyz'
        ans = []
        self.dfs(digits, 0, mem, "", ans)
        return ans

    def dfs(self, digits, start, mem, out, ans):
        if len(out)==len(digits):
            ans.append(out)
            return
        for ch in mem[digits[start]]:
            self.dfs(digits, start+1, mem, out+ch, ans)
        
#leetcode submit region end(Prohibit modification and deletion)
