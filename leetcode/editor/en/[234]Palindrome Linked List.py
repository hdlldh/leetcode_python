#Given a singly linked list, determine if it is a palindrome. 
#
# Example 1: 
#
# 
#Input: 1->2
#Output: false 
#
# Example 2: 
#
# 
#Input: 1->2->2->1
#Output: true 
#
# Follow up: 
#Could you do it in O(n) time and O(1) space? 
# Related Topics Linked List Two Pointers



#leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next: return True
        p1 = head
        p2 = head
        while p2.next and p2.next.next:
            p1 = p1.next
            p2 = p2.next.next
        head2 = p1.next
        p1.next = None

        pre = head2
        cur = head2.next
        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        head2.next = None

        p = head
        q = pre
        while p and q:
            if p.val != q.val: return False
            p = p.next
            q = q.next
        return True





#leetcode submit region end(Prohibit modification and deletion)
