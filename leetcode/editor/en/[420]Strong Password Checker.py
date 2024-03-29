# A password is considered strong if below conditions are all met: 
# 
#  
#  It has at least 6 characters and at most 20 characters. 
#  It must contain at least one lowercase letter, at least one uppercase letter,
#  and at least one digit. 
#  It must NOT contain three repeating characters in a row ("...aaa..." is weak,
#  but "...aa...a..." is strong, assuming other conditions are met). 
#  
# 
#  Write a function strongPasswordChecker(s), that takes a string s as input, an
# d return the MINIMUM change required to make s a strong password. If s is alread
# y strong, return 0. 
# 
#  Insertion, deletion or replace of any one character are all considered as one
#  change.


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def strongPasswordChecker(self, s):
        """
        :type s: str
        :rtype: int
        """
        
# leetcode submit region end(Prohibit modification and deletion)
