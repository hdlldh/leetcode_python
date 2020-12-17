# You have some coins. The i-th coin has a probability prob[i] of facing heads w
# hen tossed. 
# 
#  Return the probability that the number of coins facing heads equals target if
#  you toss every coin exactly once. 
# 
#  
#  Example 1: 
#  Input: prob = [0.4], target = 1
# Output: 0.40000
#  Example 2: 
#  Input: prob = [0.5,0.5,0.5,0.5,0.5], target = 0
# Output: 0.03125
#  
#  
#  Constraints: 
# 
#  
#  1 <= prob.length <= 1000 
#  0 <= prob[i] <= 1 
#  0 <= target <= prob.length 
#  Answers will be accepted as correct if they are within 10^-5 of the correct a
# nswer. 
#  
#  Related Topics Math Dynamic Programming


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def probabilityOfHeads(self, prob, target):
        """
        :type prob: List[float]
        :type target: int
        :rtype: float
        """
        
# leetcode submit region end(Prohibit modification and deletion)
