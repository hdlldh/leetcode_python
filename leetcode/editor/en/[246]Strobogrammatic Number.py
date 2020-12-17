#A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down). 
#
# Write a function to determine if a number is strobogrammatic. The number is represented as a string. 
#
# Example 1: 
#
# 
#Input:  "69"
#Output: true
# 
#
# Example 2: 
#
# 
#Input:  "88"
#Output: true 
#
# Example 3: 
#
# 
#Input:  "962"
#Output: false 
# Related Topics Hash Table Math



#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        mem = {'6': '9', '9': '6', '8': '8', '1': '1', '0': '0'}
        n = len(num)
        if n % 2 == 0:

            r = n // 2
            l = r - 1
        else:
            mid = n // 2
            if num[mid] not in ['0', '1', '8']: return False
            l = mid - 1
            r = mid + 1

        while l >= 0:
            if num[l] not in mem or mem[num[l]] != num[r]: return False
            l -= 1
            r += 1
        return True
        
#leetcode submit region end(Prohibit modification and deletion)
