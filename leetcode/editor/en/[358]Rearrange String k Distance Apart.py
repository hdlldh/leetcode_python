#Given a non-empty string s and an integer k, rearrange the string such that the same characters are at least distance k from each other. 
#
# All input strings are given in lowercase letters. If it is not possible to rearrange the string, return an empty string "". 
#
# Example 1: 
#
# 
# 
#Input: s = "aabbcc", k = 3
#Output: "abcabc" 
#Explanation: The same letters are at least distance 3 from each other.
# 
#
# 
# Example 2: 
#
# 
#Input: s = "aaabc", k = 3
#Output: "" 
#Explanation: It is not possible to rearrange the string.
# 
#
# 
# Example 3: 
#
# 
#Input: s = "aaadbbcc", k = 2
#Output: "abacabcd"
#Explanation: The same letters are at least distance 2 from each other.
# 
# 
# 
# Related Topics Hash Table Heap Greedy


import collections
import heapq
#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def rearrangeString(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        counter = collections.Counter(s)
        heap = []
        buff = collections.deque()
        ans = ''

        for ch, cnt in counter.items():
            heapq.heappush(heap, (-cnt, ch))
        while heap:
            cnt, ch = heapq.heappop(heap)
            ans += ch
            cnt += 1
            buff.append((cnt, ch))
            if len(buff) >= k:
                cnt, ch = buff.popleft()
                if cnt != 0:
                    heapq.heappush(heap, (cnt, ch))
        if len(ans) != len(s): return ''
        return ans
#leetcode submit region end(Prohibit modification and deletion)
