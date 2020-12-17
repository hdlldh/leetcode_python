# You are given a circular array nums of positive and negative integers. If a nu
# mber k at an index is positive, then move forward k steps. Conversely, if it's n
# egative (-k), move backward k steps. Since the array is circular, you may assume
#  that the last element's next element is the first element, and the first elemen
# t's previous element is the last element. 
# 
#  Determine if there is a loop (or a cycle) in nums. A cycle must start and end
#  at the same index and the cycle's length > 1. Furthermore, movements in a cycle
#  must all follow a single direction. In other words, a cycle must not consist of
#  both forward and backward movements. 
# 
#  
# 
#  Example 1: 
# 
#  
# Input: [2,-1,1,2,2]
# Output: true
# Explanation: There is a cycle, from index 0 -> 2 -> 3 -> 0. The cycle's length
#  is 3.
#  
# 
#  Example 2: 
# 
#  
# Input: [-1,2]
# Output: false
# Explanation: The movement from index 1 -> 1 -> 1 ... is not a cycle, because t
# he cycle's length is 1. By definition the cycle's length must be greater than 1.
# 
#  
# 
#  Example 3: 
# 
#  
# Input: [-2,1,-1,-2,-2]
# Output: false
# Explanation: The movement from index 1 -> 2 -> 1 -> ... is not a cycle, becaus
# e movement from index 1 -> 2 is a forward movement, but movement from index 2 ->
#  1 is a backward movement. All movements in a cycle must follow a single directi
# on. 
# 
#  
# 
#  Note: 
# 
#  
#  -1000 ≤ nums[i] ≤ 1000 
#  nums[i] ≠ 0 
#  1 ≤ nums.length ≤ 5000 
#  
# 
#  
# 
#  Follow up: 
# 
#  Could you solve it in O(n) time complexity and O(1) extra space complexity? R
# elated Topics Array Two Pointers


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def circularArrayLoop(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        visited = set()
        n = len(nums)
        for i, num in enumerate(nums):
            if i in visited: continue
            slow = i
            fast = i

            while True:
                if slow in visited: break
                visited.add(slow)
                slow = (slow + nums[slow]) % n
                tmp = (fast + nums[fast]) % n
                fast = (tmp + nums[tmp]) % n
                if num > 0 and (nums[tmp] < 0 or nums[fast] < 0): break
                if num < 0 and (nums[tmp] > 0 or nums[fast] > 0): break
                if slow == fast:
                    if slow == (slow + nums[slow]) % n: break
                    return True
        return False
        
# leetcode submit region end(Prohibit modification and deletion)
