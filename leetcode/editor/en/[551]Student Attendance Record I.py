# You are given a string representing an attendance record for a student. The re
# cord only contains the following three characters:
# 
#  
#  
#  'A' : Absent. 
#  'L' : Late. 
#  'P' : Present. 
#  
#  
# 
#  
# A student could be rewarded if his attendance record doesn't contain more than
#  one 'A' (absent) or more than two continuous 'L' (late). 
# 
#  You need to return whether the student could be rewarded according to his att
# endance record. 
# 
#  Example 1: 
#  
# Input: "PPALLP"
# Output: True
#  
#  
# 
#  Example 2: 
#  
# Input: "PPALLL"
# Output: False
#  
#  
# 
# 
#  Related Topics String


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        count_A = 0
        count_L = 0
        for i, ch in enumerate(s):
            if ch=='A':
                count_A +=1
                if count_A>1: return False
            if ch=='L':
                if i>0 and s[i-1]=='L':
                    count_L += 1
                    if count_L>1: return False
                else:
                    count_L = 0
        return True
        
# leetcode submit region end(Prohibit modification and deletion)
