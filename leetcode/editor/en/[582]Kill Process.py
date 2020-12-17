# Given n processes, each process has a unique PID (process id) and its PPID (pa
# rent process id). 
# 
#  Each process only has one parent process, but may have one or more children p
# rocesses. This is just like a tree structure. Only one process has PPID that is 
# 0, which means this process has no parent process. All the PIDs will be distinct
#  positive integers. 
# 
#  We use two list of integers to represent a list of processes, where the first
#  list contains PID for each process and the second list contains the correspondi
# ng PPID. 
#  
#  Now given the two lists, and a PID representing a process you want to kill, r
# eturn a list of PIDs of processes that will be killed in the end. You should ass
# ume that when a process is killed, all its children processes will be killed. No
#  order is required for the final answer. 
# 
#  Example 1: 
#  
# Input: 
# pid =  [1, 3, 10, 5]
# ppid = [3, 0, 5, 3]
# kill = 5
# Output: [5,10]
# Explanation: 
#            3
#          /   \
#         1     5
#              /
#             10
# Kill 5 will also kill 10.
#  
#  
# 
#  Note: 
#  
#  The given kill id is guaranteed to be one of the given PIDs. 
#  n >= 1. 
#  
#  Related Topics Tree Queue


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def killProcess(self, pid, ppid, kill):
        """
        :type pid: List[int]
        :type ppid: List[int]
        :type kill: int
        :rtype: List[int]
        """
        tree = collections.defaultdict(set)
        for cur, par in zip(pid, ppid):
            tree[par].add(cur)

        ans = []
        queue = collections.deque()
        queue.append(kill)
        visited = set()
        visited.add(kill)
        while queue:
            p = queue.popleft()
            ans.append(p)
            for c in tree[p]:
                if c in visited: continue
                queue.append(c)
                visited.add(c)
        return ans

        
# leetcode submit region end(Prohibit modification and deletion)
