#Remove all elements from a linked list of integers that have value val. 
#
# Example: 
#
# 
#Input:  1->2->6->3->4->5->6, val = 6
#Output: 1->2->3->4->5
# 
# Related Topics Linked List



#leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy
        cur = head
        while cur:
            if cur.val != val:
                pre.next = cur
                pre= pre.next
            cur = cur.next
        pre.next = None
        return dummy.next
#leetcode submit region end(Prohibit modification and deletion)
