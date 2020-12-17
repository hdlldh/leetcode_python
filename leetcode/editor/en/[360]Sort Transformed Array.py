#Given a sorted array of integers nums and integer values a, b and c. Apply a quadratic function of the form f(x) = ax2 + bx + c to each element x in the array. 
#
# The returned array must be in sorted order. 
#
# Expected time complexity: O(n) 
#
# 
# Example 1: 
#
# 
#Input: nums = [-4,-2,2,4], a = 1, b = 3, c = 5
#Output: [3,9,15,33]
# 
#
# 
# Example 2: 
#
# 
#Input: nums = [-4,-2,2,4], a = -1, b = 3, c = 5
#Output: [-23,-5,1,7]
# 
# 
# Related Topics Math Two Pointers



#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def sortTransformedArray(self, nums, a, b, c):
        """
        :type nums: List[int]
        :type a: int
        :type b: int
        :type c: int
        :rtype: List[int]
        """
        n = len(nums)
        ans = [c]*n
        n = len(nums)
        ans = [0] * n
        if a == 0:
            if b >= 0:
                for i, num in enumerate(nums): ans[i] = b * num + c
            elif b < 0:
                for i, num in enumerate(nums): ans[n - i - 1] = b * num + c
        else:
            l = 0
            r = n-1
            if a>0:
                k = n-1
                while l<=r:
                    if self.calc(nums[l], a, b, c) < self.calc(nums[r], a, b, c):
                        ans[k] = self.calc(nums[r], a, b, c)
                        r-=1
                        k-=1
                    else:
                        ans[k] = self.calc(nums[l], a, b, c)
                        l+=1
                        k-=1
            else:
                k = 0
                while l<=r:
                    if self.calc(nums[l], a, b, c) < self.calc(nums[r], a, b, c):
                        ans[k] = self.calc(nums[l], a, b, c)
                        l+=1
                        k+=1
                    else:
                        ans[k] = self.calc(nums[r], a, b, c)
                        r-=1
                        k+=1
        return ans

    def calc(self, x, a, b, c): return a*x*x+b*x+c
        
#leetcode submit region end(Prohibit modification and deletion)
