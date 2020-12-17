# A string S represents a list of words. 
# 
#  Each letter in the word has 1 or more options. If there is one option, the le
# tter is represented as is. If there is more than one option, then curly braces d
# elimit the options. For example, "{a,b,c}" represents options ["a", "b", "c"]. 
# 
#  For example, "{a,b,c}d{e,f}" represents the list ["ade", "adf", "bde", "bdf",
#  "cde", "cdf"]. 
# 
#  Return all words that can be formed in this manner, in lexicographical order.
#  
# 
#  
# 
#  Example 1: 
# 
#  
# Input: "{a,b}c{d,e}f"
# Output: ["acdf","acef","bcdf","bcef"]
#  
# 
#  Example 2: 
# 
#  
# Input: "abcd"
# Output: ["abcd"]
#  
# 
#  
# 
#  Note: 
# 
#  
#  1 <= S.length <= 50 
#  There are no nested curly brackets. 
#  All characters inside a pair of consecutive opening and ending curly brackets
#  are different. 
#  
#  Related Topics Backtracking


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def expand(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        if not S: return []
        if '{' not in S: return [S]
        start = S.index('{')
        end = S.index('}')
        subset = S[start+1:end].split(',')
        left = [S[:start]+s for s in subset]
        right = self.expand(S[end+1:])
        if not right: return left
        ans = []
        for l in left:
            for r in right:
                ans.append(l+r)
        ans.sort()
        return ans
        
# leetcode submit region end(Prohibit modification and deletion)
