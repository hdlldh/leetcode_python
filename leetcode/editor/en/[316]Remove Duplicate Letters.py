#Given a string which contains only lowercase letters, remove duplicate letters so that every letter appears once and only once. You must make sure your result is the smallest in lexicographical order among all possible results. 
#
# Example 1: 
#
# 
#Input: "bcabc"
#Output: "abc"
# 
#
# Example 2: 
#
# 
#Input: "cbacdcbc"
#Output: "acdb"
# 
# Related Topics Stack Greedy



#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        last_pos = {}
        for i, ch in enumerate(s):
            last_pos[ch] = i

        stack = []
        seen = set()
        for i, ch in enumerate(s):
            if ch in seen: continue
            while stack and ch < stack[-1] and i < last_pos[stack[-1]]:
                seen.remove(stack.pop())
            stack.append(ch)
            seen.add(ch)
        return ''.join(stack)
        
#leetcode submit region end(Prohibit modification and deletion)
