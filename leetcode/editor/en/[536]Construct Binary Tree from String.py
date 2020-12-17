# You need to construct a binary tree from a string consisting of parenthesis an
# d integers. 
# 
#  The whole input represents a binary tree. It contains an integer followed by 
# zero, one or two pairs of parenthesis. The integer represents the root's value a
# nd a pair of parenthesis contains a child binary tree with the same structure. 
# 
#  You always start to construct the left child node of the parent first if it e
# xists. 
# 
#  Example: 
#  
# Input: "4(2(3)(1))(6(5))"
# Output: return the tree root node representing the following tree:
# 
#        4
#      /   \
#     2     6
#    / \   / 
#   3   1 5   
#  
#  
# 
#  Note: 
#  
#  There will only be '(', ')', '-' and '0' ~ '9' in the input string. 
#  An empty tree is represented by "" instead of "()". 
#  
#  Related Topics String Tree


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def str2tree(self, s):
        """
        :type s: str
        :rtype: TreeNode
        """
        if not s: return None
        n = len(s)
        i = 0
        val = 0
        sign = 1
        while i<n and (s[i]>='0' and s[i]<='9' or s[i]=='-'):
            if s[i] == '-':
                sign = -1
                i+=1
                continue
            val = val*10 + ord(s[i]) - ord('0')
            i+=1
        node = TreeNode(val*sign)
        cnt = 0
        left = i
        while i<n:
            if s[i] =='(': cnt+=1
            elif s[i]==')':
                cnt-=1
                if cnt ==0:
                    node.left = self.str2tree(s[left+1:i])
                    break
            i+=1
        cnt = 0
        i +=1
        left = i
        while i<n:
            if s[i] =='(': cnt+=1
            elif s[i]==')':
                cnt-=1
                if cnt ==0:
                    node.right = self.str2tree(s[left+1:i])
                    break
            i+=1
        return node
# leetcode submit region end(Prohibit modification and deletion)
