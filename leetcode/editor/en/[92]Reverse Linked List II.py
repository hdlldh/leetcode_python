#Reverse a linked list from position m to n. Do it in one-pass. 
#
# Note: 1 ≤ m ≤ n ≤ length of list. 
#
# Example: 
#
# 
#Input: 1->2->3->4->5->NULL, m = 2, n = 4
#Output: 1->4->3->2->5->NULL
# 
# Related Topics Linked List



#leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        id = 1
        cur = dummy.next
        pre = dummy
        pre1 = None
        cur1 = None
        while id <= n:
            if id==m:
                pre1 = pre
                cur1 = cur
            if id<=m:
                pre = cur
                cur = cur.next
            else:
                tmp = cur.next
                cur.next = pre
                pre = cur
                cur = tmp
            id+=1
        pre1.next = pre
        cur1.next = cur
        return dummy.next
        
#leetcode submit region end(Prohibit modification and deletion)
