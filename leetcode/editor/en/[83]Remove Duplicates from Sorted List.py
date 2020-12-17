#Given a sorted linked list, delete all duplicates such that each element appear only once. 
#
# Example 1: 
#
# 
#Input: 1->1->2
#Output: 1->2
# 
#
# Example 2: 
#
# 
#Input: 1->1->2->3->3
#Output: 1->2->3
# 
# Related Topics Linked List



#leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next: return head
        p1 = head
        p2 = head.next
        while p2:
            if p2.val!=p1.val:
                p1.next = p2
                p1 = p2
            p2 = p2.next
        p1.next = None
        return head
        
#leetcode submit region end(Prohibit modification and deletion)
