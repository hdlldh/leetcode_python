# Given an array nums sorted in ascending order, return true if and only if you 
# can split it into 1 or more subsequences such that each subsequence consists of 
# consecutive integers and has length at least 3. 
# 
#  
# 
#  Example 1: 
# 
#  
# Input: [1,2,3,3,4,5]
# Output: True
# Explanation:
# You can split them into two consecutive subsequences : 
# 1, 2, 3
# 3, 4, 5
# 
#  
# 
#  Example 2: 
# 
#  
# Input: [1,2,3,3,4,4,5,5]
# Output: True
# Explanation:
# You can split them into two consecutive subsequences : 
# 1, 2, 3, 4, 5
# 3, 4, 5
# 
#  
# 
#  Example 3: 
# 
#  
# Input: [1,2,3,4,4,5]
# Output: False
#  
# 
#  
# 
#  Constraints: 
# 
#  
#  1 <= nums.length <= 10000 
#  
# 
#  
#  Related Topics Heap Greedy


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def isPossible(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        freq = collections.Counter(nums)
        need = collections.Counter()
        for num in nums:
            if freq[num] == 0: continue
            if need[num] > 0:
                need[num]-=1
                need[num+1]+=1
            elif freq[num+1]>0 and freq[num+2]>0:
                freq[num+1] -=1
                freq[num+2] -=1
                need[num+3] +=1
            else:return False
            freq[num] -=1
        return True
# leetcode submit region end(Prohibit modification and deletion)
