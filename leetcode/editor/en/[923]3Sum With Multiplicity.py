#Given an integer array A, and an integer target, return the number of tuples i,
# j, k such that i < j < k and A[i] + A[j] + A[k] == target. 
#
# As the answer can be very large, return it modulo 10^9 + 7. 
#
# 
#
# Example 1: 
#
# 
#Input: A = [1,1,2,2,3,3,4,4,5,5], target = 8
#Output: 20
#Explanation: 
#Enumerating by the values (A[i], A[j], A[k]):
#(1, 2, 5) occurs 8 times;
#(1, 3, 4) occurs 8 times;
#(2, 2, 4) occurs 2 times;
#(2, 3, 3) occurs 2 times.
# 
#
# 
# Example 2: 
#
# 
#Input: A = [1,1,2,2,2,2], target = 5
#Output: 12
#Explanation: 
#A[i] = 1, A[j] = A[k] = 2 occurs 12 times:
#We choose one 1 from [1,1] in 2 ways,
#and two 2s from [2,2,2,2] in 6 ways.
# 
#
# 
# 
#
# Note: 
#
# 
# 3 <= A.length <= 3000 
# 0 <= A[i] <= 100 
# 0 <= target <= 300 
# Related Topics Two Pointers




#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def threeSumMulti(self, A, target):
        """
        :type A: List[int]
        :type target: int
        :rtype: int
        """
        maxA = 100
        kMod = 1000000007
        count = [0] * (maxA + 1)
        for num in A: count[num] += 1
        ans = 0
        for i in range(maxA + 1):
            if not count[i]: continue
            for j in range(i, maxA + 1):
                if not count[j]: continue
                k = target - i - j
                if k < j or k > maxA: continue
                if not count[k]: continue
                if i == j == k and count[i] >= 3:
                    ans += count[i] * (count[i] - 1) * (count[i] - 2) // 6
                elif i == j != k and count[i] >= 2:
                    ans += count[i] * (count[i] - 1) // 2 * count[k]
                elif i != j == k and count[j] >= 2:
                    ans += count[j] * (count[j] - 1) // 2 * count[i]
                elif i != j != k:
                    ans += count[i] * count[j] * count[k]
        return ans % kMod
        
#leetcode submit region end(Prohibit modification and deletion)
