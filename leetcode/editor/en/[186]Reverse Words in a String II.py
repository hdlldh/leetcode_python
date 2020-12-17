#Given an input string , reverse the string word by word. 
#
# Example: 
#
# 
#Input:  ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]
#Output: ["b","l","u","e"," ","i","s"," ","s","k","y"," ","t","h","e"] 
#
# Note: 
#
# 
# A word is defined as a sequence of non-space characters. 
# The input string does not contain leading or trailing spaces. 
# The words are always separated by a single space. 
# 
#
# Follow up: Could you do it in-place without allocating extra space? 
# Related Topics String



#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        n = len(s)
        i = -1
        j = 0
        while j<n:
            if s[j]==' ':
                self.revserse(s,i+1,j-1)
                i = j
            j+=1
        self.revserse(s, i + 1, n-1)
        self.revserse(s, 0, n-1)

    def revserse(self, s, start, end):
        left = start
        right = end
        while left<right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -=1
        
#leetcode submit region end(Prohibit modification and deletion)
