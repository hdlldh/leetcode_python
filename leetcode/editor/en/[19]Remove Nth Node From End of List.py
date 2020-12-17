#Given a linked list, remove the n-th node from the end of list and return its head. 
#
# Example: 
#
# 
#Given linked list: 1->2->3->4->5, and n = 2.
#
#After removing the second node from the end, the linked list becomes 1->2->3->5.
# 
#
# Note: 
#
# Given n will always be valid. 
#
# Follow up: 
#
# Could you do this in one pass? 
# Related Topics Linked List Two Pointers



#leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        p1 = dummy
        p2 = dummy
        for _ in range(n+1): p1 = p1.next
        while p1:
            p1 = p1.next
            p2 = p2.next
        p2.next = p2.next.next
        return dummy.next
#leetcode submit region end(Prohibit modification and deletion)
