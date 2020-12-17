#We are given a binary tree (with root node root), a target node, and an integer
# value K. 
#
# Return a list of the values of all nodes that have a distance K from the targe
#t node. The answer can be returned in any order. 
#
# 
#
# 
# 
#
# 
# Example 1: 
#
# 
#Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, K = 2
#
#Output: [7,4,1]
#
#Explanation: 
#The nodes that are a distance 2 from the target node (with value 5)
#have values 7, 4, and 1.
#
#
#
#Note that the inputs "root" and "target" are actually TreeNodes.
#The descriptions of the inputs above are just serializations of these objects.
# 
#
# 
#
# Note: 
#
# 
# The given tree is non-empty. 
# Each node in the tree has unique values 0 <= node.val <= 500. 
# The target node is a node in the tree. 
# 0 <= K <= 1000. 
# 
# 
# Related Topics Tree Depth-first Search Breadth-first Search




#leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def distanceK(self, root, target, K):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type K: int
        :rtype: List[int]
        """
        graph = collections.defaultdict(set)
        self.buildGraph(None, root, graph)
        queue = collections.deque()
        queue.append(target.val)
        visited = set()
        visited.add(target.val)
        steps = 0
        while queue:
            size = len(queue)
            if steps == K: return list(queue)
            steps += 1
            if steps>K: break
            for _ in range(size):
                u = queue.popleft()
                for v in graph[u]:
                    if v in visited: continue
                    queue.append(v)
                    visited.add(v)
        return list(queue)

    def buildGraph(self, parent, child, graph):
        if parent:
            graph[parent.val].add(child.val)
            graph[child.val].add(parent.val)
        if child.left: self.buildGraph(child, child.left,graph)
        if child.right: self.buildGraph(child, child.right,graph)
        
#leetcode submit region end(Prohibit modification and deletion)
