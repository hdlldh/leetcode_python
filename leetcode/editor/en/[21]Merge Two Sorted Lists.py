#Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists. 
#
# Example:
# 
#Input: 1->2->4, 1->3->4
#Output: 1->1->2->3->4->4
# 
# Related Topics Linked List



#leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        p = dummy
        while l1 and l2:
            if l1.val<=l2.val:
                p.next = l1
                l1 = l1.next
            else:
                p.next = l2
                l2 = l2.next
            p = p.next
        if l1: p.next = l1
        if l2: p.next = l2
        return dummy.next
        
#leetcode submit region end(Prohibit modification and deletion)
