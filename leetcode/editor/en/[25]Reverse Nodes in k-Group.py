#Given a linked list, reverse the nodes of a linked list k at a time and return its modified list. 
#
# k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is. 
#
# 
# 
#
# Example: 
#
# Given this linked list: 1->2->3->4->5 
#
# For k = 2, you should return: 2->1->4->3->5 
#
# For k = 3, you should return: 3->2->1->4->5 
#
# Note: 
#
# 
# Only constant extra memory is allowed. 
# You may not alter the values in the list's nodes, only nodes itself may be changed. 
# 
# Related Topics Linked List



#leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if k==1: return head
        return self.helper(head, k)

    def helper(self, head, k):
        if not head or not head.next: return head
        cnt = 0
        p = head
        while p:
            cnt += 1
            if cnt ==k: break
            p = p.next
        if cnt<k: return head

        pre = head
        cur = head.next
        while cur:
            cnt -= 1
            if cnt==0: break
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        head.next = self.helper(cur, k)
        return pre

#leetcode submit region end(Prohibit modification and deletion)
