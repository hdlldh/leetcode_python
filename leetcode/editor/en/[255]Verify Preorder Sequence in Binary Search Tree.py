#Given an array of numbers, verify whether it is the correct preorder traversal sequence of a binary search tree. 
#
# You may assume each number in the sequence is unique. 
#
# Consider the following binary search tree: 
#
# 
#     5
#    / \
#   2   6
#  / \
# 1   3 
#
# Example 1: 
#
# 
#Input: [5,2,6,1,3]
#Output: false 
#
# Example 2: 
#
# 
#Input: [5,2,1,3,6]
#Output: true 
#
# Follow up: 
#Could you do it using only constant space complexity? 
# Related Topics Stack Tree



#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def verifyPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: bool
        """
        low = -float('inf')
        stack = []
        for num in preorder:
            if num < low: return False
            while stack and num >stack[-1]:
                low = stack.pop()
            stack.append(num)
            #print(stack)
        return True


    def verifyPreorder2(self, preorder): # TLE
        """
        :type preorder: List[int]
        :rtype: bool
        """
        return self.helper(preorder, 0, len(preorder)-1, -float('inf'), float('inf'))

    def helper(self, preorder, start, end, lower, upper):
        #print(start, end, lower, upper)
        if start>end: return True
        val = preorder[start]
        if val >= upper or val <= lower: return False
        if start==end: return True
        i = start +1
        while i<=end and preorder[i]< val: i+=1
        return self.helper(preorder, start+1, i-1, lower, val) and self.helper(preorder, i, end, val, upper)
        
#leetcode submit region end(Prohibit modification and deletion)
