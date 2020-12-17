#Shuffle a set of numbers without duplicates.
# 
#
# Example:
# 
#// Init an array with set 1, 2, and 3.
#int[] nums = {1,2,3};
#Solution solution = new Solution(nums);
#
#// Shuffle the array [1,2,3] and return its result. Any permutation of [1,2,3] must equally likely to be returned.
#solution.shuffle();
#
#// Resets the array back to its original configuration [1,2,3].
#solution.reset();
#
#// Returns the random shuffling of array [1,2,3].
#solution.shuffle();
# 
#



#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        self.size = len(nums)

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        return self.nums
        

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        ans = self.nums[:]
        for i in range(self.size-1,0,-1):
            j = random.randint(0, i)
            if i!=j: ans[i], ans[j] = ans[j], ans[i]
        return ans
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
#leetcode submit region end(Prohibit modification and deletion)
