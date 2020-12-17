#Given a linked list, return the node where the cycle begins. If there is no cycle, return null. 
#
# To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed) in the linked list where tail connects to. If pos is -1, then there is no cycle in the linked list. 
#
# Note: Do not modify the linked list. 
#
# 
#
# Example 1: 
#
# 
#Input: head = [3,2,0,-4], pos = 1
#Output: tail connects to node index 1
#Explanation: There is a cycle in the linked list, where tail connects to the second node.
# 
#
# 
#
# Example 2: 
#
# 
#Input: head = [1,2], pos = 0
#Output: tail connects to node index 0
#Explanation: There is a cycle in the linked list, where tail connects to the first node.
# 
#
# 
#
# Example 3: 
#
# 
#Input: head = [1], pos = -1
#Output: no cycle
#Explanation: There is no cycle in the linked list.
# 
#
# 
#
# 
#
# Follow-up: 
#Can you solve it without using extra space? 
# Related Topics Linked List Two Pointers



#leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        p1 = head
        p2 = head
        hasCycle = False
        while p2 and p2.next:
            p1 = p1.next
            p2 = p2.next.next
            if p1 == p2:
                hasCycle = True
                break
        if not hasCycle: return None
        p2 = head
        while p1!=p2:
            p1 = p1.next
            p2 = p2.next
        return p1
        
#leetcode submit region end(Prohibit modification and deletion)
