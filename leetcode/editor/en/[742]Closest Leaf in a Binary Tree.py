#Given a binary tree where every node has a unique value, and a target key k, find the value of the nearest leaf node to target k in the tree.
# 
#Here, nearest to a leaf means the least number of edges travelled on the binary tree to reach any leaf of the tree. Also, a node is called a leaf if it has no children.
# 
#In the following examples, the input tree is represented in flattened form row by row.
#The actual root tree given will be a TreeNode object.
# 
#Example 1:
# 
#Input:
#root = [1, 3, 2], k = 1
#Diagram of binary tree:
#          1
#         / \
#        3   2
#
#Output: 2 (or 3)
#
#Explanation: Either 2 or 3 is the nearest leaf node to the target of 1.
# 
# 
#Example 2:
# 
#Input:
#root = [1], k = 1
#Output: 1
#
#Explanation: The nearest leaf node is the root node itself.
# 
# 
#
# 
#Example 3:
# 
#Input:
#root = [1,2,3,4,null,null,null,5,null,6], k = 2
#Diagram of binary tree:
#             1
#            / \
#           2   3
#          /
#         4
#        /
#       5
#      /
#     6
#
#Output: 3
#Explanation: The leaf node with value 3 (and not the leaf node with value 6) is nearest to the node with value 2.
# 
# 
#
# Note: 
# 
# root represents a binary tree with at least 1 node and at most 1000 nodes. 
# Every node has a unique node.val in range [1, 1000]. 
# There exists some node in the given binary tree for which node.val == k. 
# 
# Related Topics Tree



#leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findClosestLeaf(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        graph = collections.defaultdict(set)
        self.target = None
        self.buildGraph(graph, root, None, k)
        queue = collections.deque()
        queue.append(self.target)
        visited = set()
        visited.add(self.target)
        while queue:
            u = queue.popleft()
            if not u.left and not u.right: return u.val
            for v in graph[u]:
                if v in visited: continue
                queue.append(v)
                visited.add(v)
        return -1

    def buildGraph(self, graph, node, parent, k):
        if not node: return
        if node.val==k: self.target = node
        if parent:
            graph[node].add(parent)
            graph[parent].add(node)
        self.buildGraph(graph, node.left, node, k)
        self.buildGraph(graph, node.right, node, k)
        
#leetcode submit region end(Prohibit modification and deletion)
