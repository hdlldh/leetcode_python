#Given a list of airline tickets represented by pairs of departure and arrival airports [from, to], reconstruct the itinerary in order. All of the tickets belong to a man who departs from JFK. Thus, the itinerary must begin with JFK. 
#
# Note: 
#
# 
# If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string. For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"]. 
# All airports are represented by three capital letters (IATA code). 
# You may assume all tickets form at least one valid itinerary. 
# 
#
# Example 1: 
#
# 
#Input: [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
#Output: ["JFK", "MUC", "LHR", "SFO", "SJC"]
# 
#
# Example 2: 
#
# 
#Input: [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
#Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]
#Explanation: Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"].
#             But it is larger in lexical order.
# 
# Related Topics Depth-first Search Graph



#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def findItinerary2(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        n = len(tickets)
        tickets.sort()
        itin = collections.defaultdict(list)
        tktCnt = collections.defaultdict(int)
        for start, end in tickets:
            itin[start].append(end)
            tktCnt[start+':'+end] += 1
        ans = ['JFK']
        self.dfs(itin, tktCnt, n, ans)
        return ans

    def dfs(self, itin, tktCnt, n, ans):
        if len(ans) == n+1: return True
        start = ans[-1]
        for end in itin[start]:
            if tktCnt[start+':'+end]>0:
                tktCnt[start + ':' + end] -= 1
                ans.append(end)
                if self.dfs(itin, tktCnt, n, ans): return True
                tktCnt[start + ':' + end] += 1
                ans.pop()
        return False

    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        hmap = {}
        ans = []
        for start, end in tickets:
            if start not in hmap: hmap[start] = []
            heapq.heappush(hmap[start], end)

        def dfs(s):
            q = hmap.get(s, None)
            while q != None and q:
                p = heapq.heappop(q)
                dfs(p)
            ans.insert(0, s)

        dfs('JFK')
        return ans
#leetcode submit region end(Prohibit modification and deletion)
