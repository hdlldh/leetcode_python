#Given a pattern and a string str, find if str follows the same pattern. 
#
# Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty substring in str. 
#
# Example 1: 
#
# 
#Input: pattern = "abab", str = "redblueredblue"
#Output: true 
#
# Example 2: 
#
# 
#Input: pattern = pattern = "aaaa", str = "asdasdasdasd"
#Output: true 
#
# Example 3: 
#
# 
#Input: pattern = "aabb", str = "xyzabcxzyabc"
#Output: false
# 
#
# Notes: 
#You may assume both pattern and str contains only lowercase letters. 
# Related Topics Backtracking



#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def wordPatternMatch(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """

        p2s = {}
        s2p = {}
        return self.dfs(pattern,str, p2s, s2p)

    def dfs(self, pattern, str, p2s, s2p):
        if not pattern and not str: return True
        if not pattern or not str: return False
        p = pattern[0]
        for i in range(1, len(str)+1):
            s = str[:i]
            if p in p2s and s in s2p:
                if p2s[p]!=s or s2p[s]!=p:continue
                if self.dfs(pattern[1:],str[i:],p2s, s2p):return True
            elif p not in p2s and s not in s2p:
                p2s[p] = s
                s2p[s] = p
                if self.dfs(pattern[1:], str[i:], p2s, s2p): return True
                p2s.pop(p)
                s2p.pop(s)
        return False
        
#leetcode submit region end(Prohibit modification and deletion)
