# There is a box protected by a password. The password is a sequence of n digits
#  where each digit can be one of the first k digits 0, 1, ..., k-1. 
# 
#  While entering a password, the last n digits entered will automatically be ma
# tched against the correct password. 
# 
#  For example, assuming the correct password is "345", if you type "012345", th
# e box will open because the correct password matches the suffix of the entered p
# assword. 
# 
#  Return any password of minimum length that is guaranteed to open the box at s
# ome point of entering it. 
# 
#  
# 
#  Example 1: 
# 
#  
# Input: n = 1, k = 2
# Output: "01"
# Note: "10" will be accepted too.
#  
# 
#  Example 2: 
# 
#  
# Input: n = 2, k = 2
# Output: "00110"
# Note: "01100", "10011", "11001" will be accepted too.
#  
# 
#  
# 
#  Note: 
# 
#  
#  n will be in the range [1, 4]. 
#  k will be in the range [1, 10]. 
#  k^n will be at most 4096. 
#  
# 
#  
#  Related Topics Math Depth-first Search


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def crackSafe(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        total = k**n + n - 1
        ans = ['0'] * n
        visited = set([''.join(ans)])
        if self.dfs(n, k, ans, total, visited): return ''.join(ans)
        return ""

    def dfs(self, n, k, ans, total, visited):
        if len(ans) == total: return True
        curr = ans[len(ans)-n+1:]

        for ch in [chr(ord('0')+i) for i in range(k)]:
            curr.append(ch)
            curr_str = ''.join(curr)
            if curr_str not in visited:
                ans.append(ch)
                visited.add(curr_str)
                if self.dfs(n, k, ans, total, visited): return True
                ans.pop()
                visited.remove(curr_str)
            curr.pop()
        return False


        
# leetcode submit region end(Prohibit modification and deletion)
