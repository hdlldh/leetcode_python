# You have some apples, where arr[i] is the weight of the i-th apple. You also h
# ave a basket that can carry up to 5000 units of weight. 
# 
#  Return the maximum number of apples you can put in the basket. 
# 
#  
#  Example 1: 
# 
#  
# Input: arr = [100,200,150,1000]
# Output: 4
# Explanation: All 4 apples can be carried by the basket since their sum of weig
# hts is 1450.
#  
# 
#  Example 2: 
# 
#  
# Input: arr = [900,950,800,1000,700,800]
# Output: 5
# Explanation: The sum of weights of the 6 apples exceeds 5000 so we choose any 
# 5 of them.
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= arr.length <= 10^3 
#  1 <= arr[i] <= 10^3 
#  
#  Related Topics Greedy


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def maxNumberOfApples(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        
# leetcode submit region end(Prohibit modification and deletion)
