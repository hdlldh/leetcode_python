# We are given a linked list with head as the first node. Let's number the nodes
#  in the list: node_1, node_2, node_3, ... etc. 
# 
#  Each node may have a next larger value: for node_i, next_larger(node_i) is th
# e node_j.val such that j > i, node_j.val > node_i.val, and j is the smallest pos
# sible choice. If such a j does not exist, the next larger value is 0. 
# 
#  Return an array of integers answer, where answer[i] = next_larger(node_{i+1})
# . 
# 
#  Note that in the example inputs (not outputs) below, arrays such as [2,1,5] r
# epresent the serialization of a linked list with a head node value of 2, second 
# node value of 1, and third node value of 5. 
# 
#  
# 
#  
#  Example 1: 
# 
#  
# Input: [2,1,5]
# Output: [5,5,0]
#  
# 
#  
#  Example 2: 
# 
#  
# Input: [2,7,4,3,5]
# Output: [7,0,5,5,0]
#  
# 
#  
#  Example 3: 
# 
#  
# Input: [1,7,5,1,9,2,5,1]
# Output: [7,9,9,9,0,5,0,0]
#  
# 
#  
# 
#  Note: 
# 
#  
#  1 <= node.val <= 10^9 for each node in the linked list. 
#  The given list has length in the range [0, 10000]. 
#  
#  
#  
#  Related Topics Linked List Stack


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def nextLargerNodes(self, head):
        """
        :type head: ListNode
        :rtype: List[int]
        """
        rightBound = []
        stack = []
        ind = 0
        p = head
        while p:
            while stack and p.val > stack[-1][1]:
                cur, _ = stack.pop()
                rightBound[cur] = p.val

            stack.append([ind, p.val])
            rightBound.append(0)
            p = p.next
            ind = ind + 1
        return rightBound
        
# leetcode submit region end(Prohibit modification and deletion)
