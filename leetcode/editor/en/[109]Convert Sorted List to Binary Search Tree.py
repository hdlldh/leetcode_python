#Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST. 
#
# For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1. 
#
# Example: 
#
# 
#Given the sorted linked list: [-10,-3,0,5,9],
#
#One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:
#
#      0
#     / \
#   -3   9
#   /   /
# -10  5
# 
# Related Topics Linked List Depth-first Search



#leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if not head: return head
        pre = None
        p1 = head
        p2 = head
        while p2.next and p2.next.next:
            pre = p1
            p1 = p1.next
            p2 = p2.next.next
        head2 = p1.next
        p1.next = None
        if pre: pre.next = None
        root = TreeNode(p1.val)
        if pre:
            pre.next = None
            root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(head2)
        return root

#leetcode submit region end(Prohibit modification and deletion)
