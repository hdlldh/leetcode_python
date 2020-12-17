# If the depth of a tree is smaller than 5, then this tree can be represented by
#  a list of three-digits integers. 
# 
#  For each integer in this list: 
# 
#  
#  The hundreds digit represents the depth D of this node, 1 <= D <= 4. 
#  The tens digit represents the position P of this node in the level it belongs
#  to, 1 <= P <= 8. The position is the same as that in a full binary tree. 
#  The units digit represents the value V of this node, 0 <= V <= 9. 
#  
# 
#  
# 
#  Given a list of ascending three-digits integers representing a binary tree wi
# th the depth smaller than 5, you need to return the sum of all paths from the ro
# ot towards the leaves. 
# 
#  Example 1: 
# 
#  
# Input: [113, 215, 221]
# Output: 12
# Explanation: 
# The tree that the list represents is:
#     3
#    / \
#   5   1
# 
# The path sum is (3 + 5) + (3 + 1) = 12.
#  
# 
#  
# 
#  Example 2: 
# 
#  
# Input: [113, 221]
# Output: 4
# Explanation: 
# The tree that the list represents is: 
#     3
#      \
#       1
# 
# The path sum is (3 + 1) = 4.
#  
# 
#  
#  Related Topics Tree


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def pathSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        levels = collections.defaultdict(dict)
        maxD = 0
        for num in nums:
            d = num //100
            p = (num //10) % 10
            v = num % 10
            levels[d][p] = v
            maxD = max(maxD, d)
        ans = 0
        #print(levels,maxD)
        for d in range(1,maxD+1):
            for p in levels[d]:
                if d !=1:
                    parent = (p - 1) // 2 + 1
                    levels[d][p] += levels[d-1][parent]
                if d == maxD or 2*p not in levels[d+1] and 2*p-1 not in levels[d+1]:
                    ans += levels[d][p]
        #print(levels)
        return ans



        
# leetcode submit region end(Prohibit modification and deletion)
