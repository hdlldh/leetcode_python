# Given a string S of digits, such as S = "123456579", we can split it into a Fi
# bonacci-like sequence [123, 456, 579]. 
# 
#  Formally, a Fibonacci-like sequence is a list F of non-negative integers such
#  that: 
# 
#  
#  0 <= F[i] <= 2^31 - 1, (that is, each integer fits a 32-bit signed integer ty
# pe); 
#  F.length >= 3; 
#  and F[i] + F[i+1] = F[i+2] for all 0 <= i < F.length - 2. 
#  
# 
#  Also, note that when splitting the string into pieces, each piece must not ha
# ve extra leading zeroes, except if the piece is the number 0 itself. 
# 
#  Return any Fibonacci-like sequence split from S, or return [] if it cannot be
#  done. 
# 
#  Example 1: 
# 
#  
# Input: "123456579"
# Output: [123,456,579]
#  
# 
#  Example 2: 
# 
#  
# Input: "11235813"
# Output: [1,1,2,3,5,8,13]
#  
# 
#  Example 3: 
# 
#  
# Input: "112358130"
# Output: []
# Explanation: The task is impossible.
#  
# 
#  Example 4: 
# 
#  
# Input: "0123"
# Output: []
# Explanation: Leading zeroes are not allowed, so "01", "2", "3" is not valid.
#  
# 
#  Example 5: 
# 
#  
# Input: "1101111"
# Output: [110, 1, 111]
# Explanation: The output [11, 0, 11, 11] would also be accepted.
#  
# 
#  Note: 
# 
#  
#  1 <= S.length <= 200 
#  S contains only digits. 
#  
#  Related Topics String Backtracking Greedy


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def splitIntoFibonacci(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        ans = []
        self.dfs(S, 0, ans)
        return ans

    def dfs(self, S, start, out):
        if start == len(S):
            if len(out)>=3:
                return True
            return False

        max_len = 1 if S[start] == '0' else 10
        num = 0
        for i in range(start, min(start+max_len, len(S))):
            num = num*10+int(S[i])
            if num > 0x7FFFFFFF: break
            if len(out) >=2:
                if num > out[-1]+ out[-2]: break
                elif num <out[-1]+ out[-2]: continue
            out.append(num)
            if self.dfs(S, i+1, out): return True
            out.pop()
        return False



        
# leetcode submit region end(Prohibit modification and deletion)
