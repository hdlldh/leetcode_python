#Given a singly linked list, group all odd nodes together followed by the even nodes. Please note here we are talking about the node number and not the value in the nodes. 
#
# You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity. 
#
# Example 1: 
#
# 
#Input: 1->2->3->4->5->NULL
#Output: 1->3->5->2->4->NULL
# 
#
# Example 2: 
#
# 
#Input: 2->1->3->5->6->4->7->NULL
#Output: 2->3->6->7->1->5->4->NULL
# 
#
# Note: 
#
# 
# The relative order inside both the even and odd groups should remain as it was in the input. 
# The first node is considered odd, the second node even and so on ... 
# 
# Related Topics Linked List



#leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next: return head
        p1 = head
        head2 = head.next
        p2 = head2
        while p2 and p2.next:
            p1.next = p1.next.next
            p1 = p1.next
            p2.next = p2.next.next
            p2 = p2.next
        p1.next = head2
        return head

        
#leetcode submit region end(Prohibit modification and deletion)
