# Return the lexicographically smallest subsequence of text that contains all th
# e distinct characters of text exactly once. 
# 
#  Example 1: 
# 
#  
# Input: "cdadabcc"
# Output: "adbc"
#  
# 
#  
#  Example 2: 
# 
#  
# Input: "abcd"
# Output: "abcd"
#  
# 
#  
#  Example 3: 
# 
#  
# Input: "ecbacba"
# Output: "eacb"
#  
# 
#  
#  Example 4: 
# 
#  
# Input: "leetcode"
# Output: "letcod"
#  
# 
#  
# 
#  Constraints: 
# 
#  
#  1 <= text.length <= 1000 
#  text consists of lowercase English letters. 
#  
# 
#  Note: This question is the same as 316: https://leetcode.com/problems/remove-
# duplicate-letters/ 
#  
#  
#  
#  Related Topics String


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def smallestSubsequence(self, text):
        """
        :type text: str
        :rtype: str
        """
        last_pos = {}
        for i, ch in enumerate(text):
            last_pos[ch] = i

        stack = []
        seen = set()
        for i, ch in enumerate(text):
            if ch in seen: continue
            while stack and ch < stack[-1] and i < last_pos[stack[-1]]:
                seen.remove(stack.pop())
            stack.append(ch)
            seen.add(ch)
        return ''.join(stack)
        
# leetcode submit region end(Prohibit modification and deletion)
