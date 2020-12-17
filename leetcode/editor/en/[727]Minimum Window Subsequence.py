#Given strings S and T, find the minimum (contiguous) substring W of S, so that T is a subsequence of W. 
#
# If there is no such window in S that covers all characters in T, return the empty string "". If there are multiple such minimum-length windows, return the one with the left-most starting index. 
#
# Example 1: 
#
# 
#Input: 
#S = "abcdebdde", T = "bde"
#Output: "bcde"
#Explanation: 
#"bcde" is the answer because it occurs before "bdde" which has the same length.
#"deb" is not a smaller window because the elements of T in the window must occur in order.
# 
#
# 
#
# Note: 
#
# 
# All the strings in the input will only contain lowercase letters. 
# The length of S will be in the range [1, 20000]. 
# The length of T will be in the range [1, 100]. 
# 
#
# Related Topics Dynamic Programming Sliding Window



#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def minWindow(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        m = len(S)
        n = len(T)
        ans = ""
        if m<n: return ans
        size = float('inf')
        # substring S[0:i] exists a subseq corresponding to T[0:j] starting at index f[i][j] of S
        f = [[-1]*(m+1) for _ in range(n+1)]
        f[0][0] = 0
        for i in range(1,m+1):
            for j in range(n+1):
                if j==0: f[0][i] = i
                else:
                    f[j][i] = f[j-1][i-1] if S[i-1]==T[j-1] else f[j][i-1]
            if f[n][i]!= -1 and i-f[n][i] < size:
                size = i-f[n][i]
                ans = S[f[n][i]:i]
        return ans









        
#leetcode submit region end(Prohibit modification and deletion)
