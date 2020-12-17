#Sort a linked list in O(n log n) time using constant space complexity. 
#
# Example 1: 
#
# 
#Input: 4->2->1->3
#Output: 1->2->3->4
# 
#
# Example 2: 
#
# 
#Input: -1->5->3->4->0
#Output: -1->0->3->4->5 
# Related Topics Linked List Sort



#leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None: return head
        pre = self.getMidNode(head)
        p1 = head
        p2 = pre.next
        pre.next = None
        p1 = self.sortList(p1)
        p2 = self.sortList(p2)
        return self.mergeList(p1, p2)

    def getMidNode(self, head):
        pre = head
        slow = head
        fast= head
        while fast and fast.next:
            pre = slow
            slow = slow.next
            fast = fast.next.next
        return pre

    def mergeList(self, p1, p2):
        dummy = ListNode(0)
        tail = dummy
        while p1 and p2:
            if p1.val > p2.val: p1, p2 = p2, p1
            tail.next = p1
            p1 = p1.next
            tail = tail.next
        if p1: tail.next = p1
        if p2: tail.next = p2
        return dummy.next

        
#leetcode submit region end(Prohibit modification and deletion)
