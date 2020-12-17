# You have k lists of sorted integers in ascending order. Find the smallest rang
# e that includes at least one number from each of the k lists. 
# 
#  We define the range [a,b] is smaller than range [c,d] if b-a < d-c or a < c i
# f b-a == d-c. 
# 
#  
# 
#  Example 1: 
# 
#  
# Input: [[4,10,15,24,26], [0,9,12,20], [5,18,22,30]]
# Output: [20,24]
# Explanation: 
# List 1: [4, 10, 15, 24,26], 24 is in range [20,24].
# List 2: [0, 9, 12, 20], 20 is in range [20,24].
# List 3: [5, 18, 22, 30], 22 is in range [20,24].
#  
# 
#  
# 
#  Note: 
# 
#  
#  The given list may contain duplicates, so ascending order means >= here. 
#  1 <= k <= 3500 
#  -105 <= value of elements <= 105. 
#  
#  Related Topics Hash Table Two Pointers String


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def smallestRange(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        k = len(nums)
        target = [1] * k
        num_list = []
        heap = []
        for i in range(k):
            if nums[i]: heapq.heappush(heap, [nums[i][0], i, 0])

        while heap:
            num, i, j = heapq.heappop(heap)
            num_list.append([num, i])
            j +=1
            if j < len(nums[i]): heapq.heappush(heap, [nums[i][j], i, j])

        left = 0
        minRange = float('inf')
        ans = []
        cnt = 0
        for i in range(len(num_list)):
            j = num_list[i][1]
            target[j] -= 1
            if target[j] >=0: cnt += 1
            while cnt == k:
                diff = num_list[i][0] - num_list[left][0]
                if diff < minRange:
                    minRange = diff
                    ans = [num_list[left][0], num_list[i][0]]
                target[num_list[left][1]] += 1
                if target[num_list[left][1]] >0: cnt -=1
                left +=1
        return ans

        
# leetcode submit region end(Prohibit modification and deletion)
