#Given a non-negative integer represented as non-empty a singly linked list of digits, plus one to the integer. 
#
# You may assume the integer do not contain any leading zero, except the number 0 itself. 
#
# The digits are stored such that the most significant digit is at the head of the list. 
#
# 
# Example : 
#
# 
#Input: [1,2,3]
#Output: [1,2,4]
# 
# 
# Related Topics Linked List



#leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def plusOne(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        self.helper(dummy)
        if dummy.val!=0: return dummy
        return dummy.next

    def helper(self, head):
        if not head: return 1
        sum = head.val + self.helper(head.next)
        head.val = sum%10
        return 1 if sum>=10 else 0

#leetcode submit region end(Prohibit modification and deletion)
