#Given a nested list of integers, return the sum of all integers in the list weighted by their depth. 
#
# Each element is either an integer, or a list -- whose elements may also be integers or other lists. 
#
# Different from the previous question where weight is increasing from root to leaf, now the weight is defined from bottom up. i.e., the leaf level integers have weight 1, and the root level integers have the largest weight. 
#
# Example 1: 
#
# 
# 
#Input: [[1,1],2,[1,1]]
#Output: 8 
#Explanation: Four 1's at depth 1, one 2 at depth 2.
# 
#
# 
# Example 2: 
#
# 
#Input: [1,[4,[6]]]
#Output: 17 
#Explanation: One 1 at depth 3, one 4 at depth 2, and one 6 at depth 1; 1*3 + 4*2 + 6*1 = 17.
# 
# 
# 
# Related Topics Depth-first Search



#leetcode submit region begin(Prohibit modification and deletion)
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution(object):
    def depthSumInverse(self, nestedList):
        """
        :type nestedList: List[NestedInteger]
        :rtype: int
        """
        mem = collections.defaultdict(int)
        self.maxDepth = 0
        self.helper(nestedList, 0, mem)
        ans = 0
        for d in mem:
            ans += mem[d] * (self.maxDepth-d+1)
        return ans

    def helper(self, nestedList, depth, mem):
        self.maxDepth = max(self.maxDepth, depth)
        for l in nestedList:
            if l.isInteger(): mem[depth]+=l.getInteger()
            else: self.helper(l.getList(), depth+1, mem)
#leetcode submit region end(Prohibit modification and deletion)
