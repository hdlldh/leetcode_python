# You are given an immutable linked list, print out all values of each node in r
# everse with the help of the following interface: 
# 
#  
#  ImmutableListNode: An interface of immutable linked list, you are given the h
# ead of the list. 
#  
# 
#  You need to use the following functions to access the linked list (you can't 
# access the ImmutableListNode directly): 
# 
#  
#  ImmutableListNode.printValue(): Print value of the current node. 
#  ImmutableListNode.getNext(): Return the next node. 
#  
# 
#  The input is only given to initialize the linked list internally. You must so
# lve this problem without modifying the linked list. In other words, you must ope
# rate the linked list using only the mentioned APIs. 
# 
#  
# 
#  Follow up: 
# 
#  Could you solve this problem in: 
# 
#  
#  Constant space complexity? 
#  Linear time complexity and less than linear space complexity? 
#  
# 
#  
#  Example 1: 
# 
#  
# Input: head = [1,2,3,4]
# Output: [4,3,2,1]
#  
# 
#  Example 2: 
# 
#  
# Input: head = [0,-4,-1,3,-5]
# Output: [-5,3,-1,-4,0]
#  
# 
#  Example 3: 
# 
#  
# Input: head = [-2,0,6,4,4,-6]
# Output: [-6,4,4,6,0,-2]
#  
# 
#  
#  
# 
#  
#  Constraints: 
# 
#  
#  The length of the linked list is between [1, 1000]. 
#  The value of each node in the linked list is between [-1000, 1000]. 
#  
# 


# leetcode submit region begin(Prohibit modification and deletion)
#   """
#   This is the ImmutableListNode's API interface.
#   You should not implement it, or speculate about its implementation.
#   """
#   class ImmutableListNode(object):
#      def printValue(self): # print the value of this node.
# .        """
#          :rtype None
#          """
#
#      def getNext(self): # return the next node.
# .        """
#          :rtype ImmutableListNode
#          """

class Solution(object):
    def printLinkedListInReverse(self, head):
        """
        :type head: ImmutableListNode
        :rtype: None
        """
		
# leetcode submit region end(Prohibit modification and deletion)
