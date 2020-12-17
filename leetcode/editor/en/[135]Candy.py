#There are N children standing in a line. Each child is assigned a rating value. 
#
# You are giving candies to these children subjected to the following requirements: 
#
# 
# Each child must have at least one candy. 
# Children with a higher rating get more candies than their neighbors. 
# 
#
# What is the minimum candies you must give? 
#
# Example 1: 
#
# 
#Input: [1,0,2]
#Output: 5
#Explanation: You can allocate to the first, second and third child with 2, 1, 2 candies respectively.
# 
#
# Example 2: 
#
# 
#Input: [1,2,2]
#Output: 4
#Explanation: You can allocate to the first, second and third child with 1, 2, 1 candies respectively.
#             The third child gets 1 candy because it satisfies the above two conditions.
# 
# Related Topics Greedy



#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        n = len(ratings)
        l2r = [1] * n
        r2l = [1] * n
        for i in range(1,n):
            if ratings[i] > ratings[i-1]:
                l2r[i] = l2r[i-1] + 1
        for i in range(n-2,-1,-1):
            if ratings[i] > ratings[i+1]:
                r2l[i] = r2l[i+1] + 1
        for i in range(n):
            l2r[i] = max(l2r[i], r2l[i])
        return sum(l2r)
        
#leetcode submit region end(Prohibit modification and deletion)
