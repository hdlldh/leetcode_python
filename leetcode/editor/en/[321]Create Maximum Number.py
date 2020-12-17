#Given two arrays of length m and n with digits 0-9 representing two numbers. Create the maximum number of length k <= m + n from digits of the two. The relative order of the digits from the same array must be preserved. Return an array of the k digits. 
#
# Note: You should try to optimize your time and space complexity. 
#
# Example 1: 
#
# 
#Input:
#nums1 = [3, 4, 6, 5]
#nums2 = [9, 1, 2, 5, 8, 3]
#k = 5
#Output:
#[9, 8, 6, 5, 3] 
#
# Example 2: 
#
# 
#Input:
#nums1 = [6, 7]
#nums2 = [6, 0, 4]
#k = 5
#Output:
#[6, 7, 6, 0, 4] 
#
# Example 3: 
#
# 
#Input:
#nums1 = [3, 9]
#nums2 = [8, 9]
#k = 3
#Output:
#[9, 8, 9]
# Related Topics Dynamic Programming Greedy



#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def maxNumber(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[int]
        """
        if k==0: return []
        n1 = len(nums1)
        n2 = len(nums2)
        ans = []
        mx = -float('inf')
        for i in range(k+1):
            j = k -i
            #print(i, j, n1, n2)
            if i > n1 or j > n2:continue
            t1 = self.maxNum(nums1, i)
            t2 = self.maxNum(nums2, j)
            t = self.mergNum(t1, t2)
            #print(t1, t2, t)
            tnum = self.getNum(t)
            if tnum > mx:
                mx = tnum
                ans = t
        return ans

    def getNum(self, nums):
        ans = 0
        for num in nums:
            ans += 10*ans + num
        return ans

    def mergNum(self, nums1, nums2):
        n1 = len(nums1)
        n2 = len(nums2)
        i = j = 0
        ans = []
        while i< n1 and j<n2:
            if nums1[i:] >= nums2[j:]:
                ans.append(nums1[i])
                i += 1
            else:
                ans.append(nums2[j])
                j += 1
        while i<n1:
            ans.append(nums1[i])
            i += 1
        while j<n2:
            ans.append(nums2[j])
            j += 1
        return ans

    def maxNum(self, nums, k):
        n = len(nums)
        drop = n-k
        stack = []
        for num in nums:
            while stack and num > stack[-1] and drop > 0:
                stack.pop()
                drop -= 1
            stack.append(num)
        while drop:
            stack.pop()
            drop -=1
        return stack
        
#leetcode submit region end(Prohibit modification and deletion)
