#Given a string S, check if the letters can be rearranged so that two characters
# that are adjacent to each other are not the same. 
#
# If possible, output any possible result. If not possible, return the empty str
#ing. 
#
# Example 1: 
#
# 
#Input: S = "aab"
#Output: "aba"
# 
#
# Example 2: 
#
# 
#Input: S = "aaab"
#Output: ""
# 
#
# Note: 
#
# 
# S will consist of lowercase letters and have length in range [1, 500]. 
# 
#
# 
# Related Topics String Heap Greedy Sort


import collections

#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def reorganizeString(self, S):
        """
        :type S: str
        :rtype: str
        """
        count = collections.Counter(S)
        n = len(S)
        ans = ""
        pq = []
        for ch in count:
            if count[ch]> (n+1)//2: return ""
            heapq.heappush(pq, [-count[ch], ch])
        while len(pq)>1:
            n1, c1 = heapq.heappop(pq)
            n2, c2 = heapq.heappop(pq)
            ans += c1
            ans += c2
            n1 += 1
            n2 += 1
            if n1!=0: heapq.heappush(pq, [n1, c1])
            if n2!=0: heapq.heappush(pq, [n2, c2])
        if pq: ans += pq[0][1]
        return ans


        
#leetcode submit region end(Prohibit modification and deletion)
