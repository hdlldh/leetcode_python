#One way to serialize a binary tree is to use pre-order traversal. When we encounter a non-null node, we record the node's value. If it is a null node, we record using a sentinel value such as #. 
#
# 
#     _9_
#    /   \
#   3     2
#  / \   / \
# 4   1  #  6
#/ \ / \   / \
## # # #   # #
# 
#
# For example, the above binary tree can be serialized to the string "9,3,4,#,#,1,#,#,2,#,6,#,#", where # represents a null node. 
#
# Given a string of comma separated values, verify whether it is a correct preorder traversal serialization of a binary tree. Find an algorithm without reconstructing the tree. 
#
# Each comma separated value in the string must be either an integer or a character '#' representing null pointer. 
#
# You may assume that the input format is always valid, for example it could never contain two consecutive commas such as "1,,3". 
#
# Example 1: 
#
# 
#Input: "9,3,4,#,#,1,#,#,2,#,6,#,#"
#Output: true 
#
# Example 2: 
#
# 
#Input: "1,#"
#Output: false
# 
#
# Example 3: 
#
# 
#Input: "9,#,#,1"
#Output: false Related Topics Stack



#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        queue = preorder.split(',')
        n = len(queue)
        cnt = 0
        for i in range(n-1):
            if queue[i] == '#':
                if cnt ==0: return False
                cnt -= 1
            else:
                cnt += 1
        return cnt == 0 and queue[-1] =='#'

    def isValidSerialization2(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        queue = []
        for s in preorder.split(','):
            queue.append(s)
            while len(queue)>=3 and queue[-1]=='#' and queue[-2]=='#' and queue[-3]!='#':
                queue.pop()
                queue.pop()
                queue.pop()
                queue.append('#')
        return queue==['#']

#leetcode submit region end(Prohibit modification and deletion)
