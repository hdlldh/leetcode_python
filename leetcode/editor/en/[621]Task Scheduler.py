# Given a char array representing tasks CPU need to do. It contains capital lett
# ers A to Z where different letters represent different tasks. Tasks could be don
# e without original order. Each task could be done in one interval. For each inte
# rval, CPU could finish one task or just be idle. 
# 
#  However, there is a non-negative cooling interval n that means between two sa
# me tasks, there must be at least n intervals that CPU are doing different tasks 
# or just be idle. 
# 
#  You need to return the least number of intervals the CPU will take to finish 
# all the given tasks. 
# 
#  
# 
#  Example: 
# 
#  
# Input: tasks = ["A","A","A","B","B","B"], n = 2
# Output: 8
# Explanation: A -> B -> idle -> A -> B -> idle -> A -> B.
#  
# 
#  
#  Constraints: 
# 
#  
#  The number of tasks is in the range [1, 10000]. 
#  The integer n is in the range [0, 100]. 
#  
#  Related Topics Array Greedy Queue


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        mx = 0
        mt = ''
        count = collections.Counter()
        for t in tasks:
            count[t] += 1
            if count[t] > mx:
                mt = t
                mx = count[t]
            elif count[t] == mx:
                mt += t
        return max(len(tasks), (mx-1)*(n+1)+len(mt))

    def leastInterval2(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        heap = []
        count = collections.Counter(tasks)
        for k, v in count.items():
            heapq.heappush(heap, [-v, k])

        ans = 0
        while heap:
            buffer = []
            i = 0
            while i<=n:
                if heap:
                    #print(heap, buffer)
                    cnt, task = heapq.heappop(heap)
                    if -cnt >1:
                        cnt += 1
                        buffer.append([cnt, task])
                ans += 1
                if not heap and not buffer: return ans
                i+=1
            for cnt, task in buffer:
                heapq.heappush(heap, [cnt, task])
        return ans

        
# leetcode submit region end(Prohibit modification and deletion)
