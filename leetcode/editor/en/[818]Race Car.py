# Your car starts at position 0 and speed +1 on an infinite number line. (Your c
# ar can go into negative positions.) 
# 
#  Your car drives automatically according to a sequence of instructions A (acce
# lerate) and R (reverse). 
# 
#  When you get an instruction "A", your car does the following: position += spe
# ed, speed *= 2. 
# 
#  When you get an instruction "R", your car does the following: if your speed i
# s positive then speed = -1 , otherwise speed = 1. (Your position stays the same.
# ) 
# 
#  For example, after commands "AAR", your car goes to positions 0->1->3->3, and
#  your speed goes to 1->2->4->-1. 
# 
#  Now for some target position, say the length of the shortest sequence of inst
# ructions to get there. 
# 
#  
# Example 1:
# Input: 
# target = 3
# Output: 2
# Explanation: 
# The shortest instruction sequence is "AA".
# Your position goes from 0->1->3.
#  
# 
#  
# Example 2:
# Input: 
# target = 6
# Output: 5
# Explanation: 
# The shortest instruction sequence is "AAARA".
# Your position goes from 0->1->3->7->7->6.
#  
# 
#  
# 
#  Note: 
# 
#  
#  1 <= target <= 10000. 
#  
#  Related Topics Dynamic Programming Heap


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def racecar(self, target):
        """
        :type target: int
        :rtype: int
        """
        dp = [float('inf')]*(target + 1)
        i = 1
        while i<=target:
            cnt1 = 1
            j = (1<<cnt1) - 1
            while j<i:
                cnt2 = 0
                k = (1 << cnt2) - 1
                while k<j:
                    dp[i] = min(dp[i], cnt1+1+cnt2+1+dp[i-j+k])
                    cnt2+=1
                    k = (1 << cnt2) - 1
                cnt1+=1
                j = (1 << cnt1) - 1
            if j==i: dp[i] = min(dp[i],cnt1)
            if j> i: dp[i] = min(dp[i], cnt1+1+dp[j-i])
            i+=1
        return dp[target]




# leetcode submit region end(Prohibit modification and deletion)
