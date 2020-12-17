# Given a non-empty array of numbers, a0, a1, a2, … , an-1, where 0 ≤ ai < 231. 
# 
# 
#  Find the maximum result of ai XOR aj, where 0 ≤ i, j < n. 
# 
#  Could you do this in O(n) runtime? 
# 
#  Example: 
# 
#  
# Input: [3, 10, 5, 25, 2, 8]
# 
# Output: 28
# 
# Explanation: The maximum result is 5 ^ 25 = 28.
#  
# 
#  
#  Related Topics Bit Manipulation Trie


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxx = 0
        mask = 0
        hashset = set()
        for i in range(31,-1,-1):
            mask |= 1<<i
            newMax = maxx | 1<<i
            for num in nums:
                hashset.add(num & mask)
            for num in hashset:
                if (num^newMax) in hashset:
                    maxx = newMax
                    break
            hashset.clear()
        return maxx
        
# leetcode submit region end(Prohibit modification and deletion)
