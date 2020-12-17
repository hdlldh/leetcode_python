#You are given two non-empty linked lists representing two non-negative integers
#. The most significant digit comes first and each of their nodes contain a singl
#e digit. Add the two numbers and return it as a linked list. 
#
# You may assume the two numbers do not contain any leading zero, except the num
#ber 0 itself. 
#
# Follow up: 
#What if you cannot modify the input lists? In other words, reversing the lists 
#is not allowed.
# 
#
# 
#Example:
# 
#Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
#Output: 7 -> 8 -> 0 -> 7
# 
# Related Topics Linked List




#leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        stack1 = []
        stack2 = []
        while l1:
            stack1.append(l1.val)
            l1 = l1.next
        while l2:
            stack2.append(l2.val)
            l2 = l2.next
        carry = 0
        sum = 0
        prev = None
        while stack1 or stack2:
            a1 = stack1.pop() if stack1 else 0
            a2 = stack2.pop() if stack2 else 0
            sum = a1 + a2 + carry
            node = ListNode(sum % 10)
            node.next = prev
            prev = node
            carry = sum//10

        if carry:
            node = ListNode(carry)
            node.next = prev
            prev = node
        return prev
        
#leetcode submit region end(Prohibit modification and deletion)
