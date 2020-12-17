#Given an encoded string, return its decoded string. 
#
# The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer. 
#
# You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc. 
#
# Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4]. 
#
# Examples: 
#
# 
#s = "3[a]2[bc]", return "aaabcbc".
#s = "3[a2[c]]", return "accaccacc".
#s = "2[abc]3[cd]ef", return "abcabccdcdcdef".
# 
#
# 
# Related Topics Stack Depth-first Search



#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s: return ""
        num_stack = []
        str_stack = [""]
        num = 0

        for ch in s:
            if ch in '0123456789':
                num = num*10+int(ch)
            elif ch == '[':
                num_stack.append(num)
                num = 0
                str_stack.append("")
            elif ch == ']':
                strg = str_stack.pop()
                k = num_stack.pop()
                str_stack[-1] += strg * k
            else:
                str_stack[-1]+=ch
        return str_stack[0]
        
#leetcode submit region end(Prohibit modification and deletion)
