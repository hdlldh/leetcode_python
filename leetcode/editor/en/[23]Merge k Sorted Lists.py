#Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity. 
#
# Example: 
#
# 
#Input:
#[
#  1->4->5,
#  1->3->4,
#  2->6
#]
#Output: 1->1->2->3->4->4->5->6
# 
# Related Topics Linked List Divide and Conquer Heap



#leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

import heapq
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        heap = []
        n = len(lists)
        dummy = ListNode(0)
        p = dummy
        for i in range(n):
            if lists[i]: heapq.heappush(heap, (lists[i].val, lists[i]))
        while heap:
            _, node = heapq.heappop(heap)
            p.next = node
            p = p.next
            if node.next:
                node = node.next
                heapq.heappush(heap, (node.val, node))
        #p.next = None
        return dummy.next


        
#leetcode submit region end(Prohibit modification and deletion)
