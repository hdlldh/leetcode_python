#Given a linked list, swap every two adjacent nodes and return its head. 
#
# You may not modify the values in the list's nodes, only nodes itself may be changed. 
#
# 
#
# Example: 
#
# 
#Given 1->2->3->4, you should return the list as 2->1->4->3.
# 
# Related Topics Linked List



#leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next: return head
        pre = head
        cur = head.next
        nxt = cur.next
        cur.next = pre
        pre.next = self.swapPairs(nxt)
        return cur

    def swapPairs2(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy0 = ListNode(0)
        dummy1 = ListNode(0)
        p0 = dummy0
        p1 = dummy1
        p = head
        odd = True
        while p:
            if odd:
                p0.next = p
                p0 = p0.next
                odd = False
            else:
                p1.next = p
                p1 = p1.next
                odd = True
            p = p.next
        p0.next = None
        p1.next = None
        dummy = ListNode(0)
        p = dummy
        odd = False
        p0 = dummy0.next
        p1 = dummy1.next
        while p0 and p1:
            if odd:
                p.next = p0
                p0 = p0.next
                odd = False
            else:
                p.next = p1
                p1 = p1.next
                odd = True
            p = p.next
        if p0: p.next = p0
        if p1: p.next = p1
        return dummy.next

        
#leetcode submit region end(Prohibit modification and deletion)
