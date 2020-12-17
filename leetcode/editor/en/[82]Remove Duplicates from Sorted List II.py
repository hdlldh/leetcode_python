#Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list. 
#
# Example 1: 
#
# 
#Input: 1->2->3->3->4->4->5
#Output: 1->2->5
# 
#
# Example 2: 
#
# 
#Input: 1->1->1->2->3
#Output: 2->3
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
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy
        cur = head
        while cur:
            while cur.next and cur.next.val == cur.val:
                cur = cur.next
            if cur!= pre.next:
                pre.next = cur.next
            else:
                pre = pre.next
            cur = cur.next
        return dummy.next

        
#leetcode submit region end(Prohibit modification and deletion)
