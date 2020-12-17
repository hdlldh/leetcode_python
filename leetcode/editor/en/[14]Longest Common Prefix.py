#Write a function to find the longest common prefix string amongst an array of strings. 
#
# If there is no common prefix, return an empty string "". 
#
# Example 1: 
#
# 
#Input: ["flower","flow","flight"]
#Output: "fl"
# 
#
# Example 2: 
#
# 
#Input: ["dog","racecar","car"]
#Output: ""
#Explanation: There is no common prefix among the input strings.
# 
#
# Note: 
#
# All given inputs are in lowercase letters a-z. 
# Related Topics String



#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        n = len(strs)
        if n==0: return ""
        if n==1: return strs[0]
        for j in range(len(strs[0])):
            for i in range(1,n):
                if j == len(strs[i]) or strs[i][j] != strs[0][j]:
                    return strs[0][:j]
        return strs[0]


#leetcode submit region end(Prohibit modification and deletion)
