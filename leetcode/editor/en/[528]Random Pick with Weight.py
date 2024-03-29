# Given an array w of positive integers, where w[i] describes the weight of inde
# x i, write a function pickIndex which randomly picks an index in proportion to i
# ts weight. 
# 
#  Note: 
# 
#  
#  1 <= w.length <= 10000 
#  1 <= w[i] <= 10^5 
#  pickIndex will be called at most 10000 times. 
#  
# 
#  Example 1: 
# 
#  
# Input: 
# ["Solution","pickIndex"]
# [[[1]],[]]
# Output: [null,0]
#  
# 
#  
#  Example 2: 
# 
#  
# Input: 
# ["Solution","pickIndex","pickIndex","pickIndex","pickIndex","pickIndex"]
# [[[1,3]],[],[],[],[],[]]
# Output: [null,0,1,1,1,0] 
#  
# 
#  Explanation of Input Syntax: 
# 
#  The input is two lists: the subroutines called and their arguments. Solution'
# s constructor has one argument, the array w. pickIndex has no arguments. Argumen
# ts are always wrapped with a list, even if there aren't any. 
#  Related Topics Binary Search Random


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):

    def __init__(self, w):
        """
        :type w: List[int]
        """
        self.sum = [0] * len(w)
        self.sum[0] = w[0]
        for i in range(1, len(w)):
            self.sum[i] = self.sum[i - 1] + w[i]

    def pickIndex(self):
        """
        :rtype: int
        """
        num = random.randint(1, self.sum[-1])
        idx = bisect.bisect_left(self.sum, num)
        return idx
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
# leetcode submit region end(Prohibit modification and deletion)
