#The Hamming distance between two integers is the number of positions at which the corresponding bits are different. 
#
# Now your job is to find the total Hamming distance between all pairs of the given numbers. 
#
#
# Example: 
# 
#Input: 4, 14, 2
#
#Output: 6
#
#Explanation: In binary representation, the 4 is 0100, 14 is 1110, and 2 is 0010 (just
#showing the four bits relevant in this case). So the answer will be:
#HammingDistance(4, 14) + HammingDistance(4, 2) + HammingDistance(14, 2) = 2 + 2 + 2 = 6.
# 
# 
#
# Note: 
# 
# Elements of the given array are in the range of 0 to 10^9
# Length of the array will not exceed 10^4. 
# 
# Related Topics Bit Manipulation



#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def totalHammingDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        stats = [0]* 32
        ans = 0
        for num in nums:
            for i in range(32):
                if num & (1<< i)==0: stats[i] += 1
        for i in range(32):
            ans += (n-stats[i])*stats[i]
        return ans
        
#leetcode submit region end(Prohibit modification and deletion)
