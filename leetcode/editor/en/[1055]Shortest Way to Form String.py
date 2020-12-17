# From any string, we can form a subsequence of that string by deleting some num
# ber of characters (possibly no deletions). 
# 
#  Given two strings source and target, return the minimum number of subsequence
# s of source such that their concatenation equals target. If the task is impossib
# le, return -1. 
# 
#  
# 
#  Example 1: 
# 
#  
# Input: source = "abc", target = "abcbc"
# Output: 2
# Explanation: The target "abcbc" can be formed by "abc" and "bc", which are sub
# sequences of source "abc".
#  
# 
#  Example 2: 
# 
#  
# Input: source = "abc", target = "acdbc"
# Output: -1
# Explanation: The target string cannot be constructed from the subsequences of 
# source string due to the character "d" in target string.
#  
# 
#  Example 3: 
# 
#  
# Input: source = "xyz", target = "xzyxz"
# Output: 3
# Explanation: The target string can be constructed as follows "xz" + "y" + "xz"
# .
#  
#  
#  Constraints: 
# 
#  
#  Both the source and target strings consist of only lowercase English letters 
# from "a"-"z". 
#  The lengths of source and target string are between 1 and 1000. 
#  Related Topics Dynamic Programming Greedy

import bisect
# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def shortestWay(self, source, target):
        """
        :type source: str
        :type target: str
        :rtype: int
        """
        m = len(source)
        n = len(target)
        mem = [[] for _ in range(26)]
        for i, ch in enumerate(source):
            mem[ord(ch)-ord('a')].append(i)

        i = 0
        j = 0
        ans = 1
        while j<n:
            tar = mem[ord(target[j]) - ord('a')]
            if not tar: return -1
            idx = bisect.bisect_left(tar, i)
            if idx == len(tar):
                i = 0
                ans +=1
            else:
                i = tar[idx] + 1
                j +=1
        return ans






# leetcode submit region end(Prohibit modification and deletion)
