# Given an array A of positive integers, call a (contiguous, not necessarily dis
# tinct) subarray of A good if the number of different integers in that subarray i
# s exactly K. 
# 
#  (For example, [1,2,3,1,2] has 3 different integers: 1, 2, and 3.) 
# 
#  Return the number of good subarrays of A. 
# 
#  
# 
#  Example 1: 
# 
#  
# Input: A = [1,2,1,2,3], K = 2
# Output: 7
# Explanation: Subarrays formed with exactly 2 different integers: [1,2], [2,1],
#  [1,2], [2,3], [1,2,1], [2,1,2], [1,2,1,2].
#  
# 
#  Example 2: 
# 
#  
# Input: A = [1,2,1,3,4], K = 3
# Output: 3
# Explanation: Subarrays formed with exactly 3 different integers: [1,2,1,3], [2
# ,1,3], [1,3,4].
#  
# 
#  
# 
#  Note: 
# 
#  
#  1 <= A.length <= 20000 
#  1 <= A[i] <= A.length 
#  1 <= K <= A.length 
#  Related Topics Hash Table Two Pointers Sliding Window


# leetcode submit region begin(Prohibit modification and deletion)
class Window(object):
    def __init__(self):
        self.count = 0
        self.data = {}

    def add(self, x):
        if x in self.data:
            self.data[x] += 1
        else:
            self.data[x] = 1
            self.count += 1

    def remove(self, x):
        self.data[x] -= 1
        if self.data[x] == 0:
            self.data.pop(x)
            self.count -= 1


class Solution(object):
    def subarraysWithKDistinct(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        n = len(A)
        ans = 0

        w1 = Window()
        l1 = 0
        w2 = Window()
        l2 = 0
        for r, x in enumerate(A):
            w1.add(x)
            w2.add(x)
            while w1.count > K:
                w1.remove(A[l1])
                l1 += 1
            while w2.count > K - 1:
                w2.remove(A[l2])
                l2 += 1
            ans += l2 - l1
        return ans
        
# leetcode submit region end(Prohibit modification and deletion)
