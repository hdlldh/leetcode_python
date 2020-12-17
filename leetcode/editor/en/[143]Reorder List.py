#Given a singly linked list L: L0→L1→…→Ln-1→Ln, 
#reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→… 
#
# You may not modify the values in the list's nodes, only nodes itself may be changed. 
#
# Example 1: 
#
# 
#Given 1->2->3->4, reorder it to 1->4->2->3. 
#
# Example 2: 
#
# 
#Given 1->2->3->4->5, reorder it to 1->5->2->4->3.
# 
# Related Topics Linked List



#leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        if not head or not head.next: return
        p1 = head
        p2 = head
        while p2 and p2.next:
            p1 = p1.next
            p2 = p2.next.next
        head2 = p1.next
        p1.next = None
        head2 = self.reverse(head2)
        return self.merge(head, head2)

    def reverse(self, head):
        if not head or not head.next: return head
        pre = head
        cur = head.next
        head.next = None
        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        return pre

    def merge(self, head1, head2):
        dummy = ListNode(0)
        p = dummy
        choice = 0
        while head1 and head2:
            if choice == 0:
                p.next = head1
                head1 = head1.next
                choice = 1
            else:
                p.next = head2
                head2 = head2.next
                choice = 0
            p = p.next
        if head1: p.next = head1
        if head2: p.next = head2
        return dummy.next

#leetcode submit region end(Prohibit modification and deletion)
