#Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x. 
#
# You should preserve the original relative order of the nodes in each of the two partitions. 
#
# Example: 
#
# 
#Input: head = 1->4->3->2->5->2, x = 3
#Output: 1->2->2->4->3->5
# 
# Related Topics Linked List Two Pointers



#leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        dummy0 = ListNode(0)
        dummy1 = ListNode(0)
        p0 = dummy0
        p1 = dummy1
        p = head
        while p:
            if p.val<x:
                p0.next = p
                p0 = p0.next
            else:
                p1.next = p
                p1 = p1.next
            p = p.next
        p1.next = None
        p0.next = dummy1.next
        return dummy0.next
        
#leetcode submit region end(Prohibit modification and deletion)
