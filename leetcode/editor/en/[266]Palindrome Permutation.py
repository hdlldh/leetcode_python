#Given a string, determine if a permutation of the string could form a palindrome. 
#
# Example 1: 
#
# 
#Input: "code"
#Output: false 
#
# Example 2: 
#
# 
#Input: "aab"
#Output: true 
#
# Example 3: 
#
# 
#Input: "carerac"
#Output: true 
# Related Topics Hash Table



#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        count = collections.Counter(s)
        oddCnt = 0
        for v in count.values():
            if v % 2: oddCnt += 1
        return oddCnt <= 1
        
#leetcode submit region end(Prohibit modification and deletion)
