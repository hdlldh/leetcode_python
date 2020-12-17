#Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and s2. 
#
# Example 1: 
#
# 
#Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
#Output: true
# 
#
# Example 2: 
#
# 
#Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
#Output: false
# 
# Related Topics String Dynamic Programming



#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):

    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        n = len(s1)
        m = len(s2)
        if (m + n) != len(s3): return False
        df = [[False] * (m + 1) for _ in range(n + 1)]
        for i in range(n + 1):
            for j in range(m + 1):
                if i == 0 and j == 0:
                    df[i][j] = True
                elif i == 0:
                    df[i][j] = df[i][j - 1] and s2[j - 1] == s3[i + j - 1]
                elif j == 0:
                    df[i][j] = df[i - 1][j] and s1[i - 1] == s3[i + j - 1]
                else:
                    df[i][j] = df[i - 1][j] and s1[i - 1] == s3[i + j - 1] or df[i][j - 1] and s2[j - 1] == s3[
                        i + j - 1]
        return df[n][m]
        
#leetcode submit region end(Prohibit modification and deletion)
