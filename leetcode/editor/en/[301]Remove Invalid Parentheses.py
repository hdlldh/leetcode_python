#Remove the minimum number of invalid parentheses in order to make the input string valid. Return all possible results. 
#
# Note: The input string may contain letters other than the parentheses ( and ). 
#
# Example 1: 
#
# 
#Input: "()())()"
#Output: ["()()()", "(())()"]
# 
#
# Example 2: 
#
# 
#Input: "(a)())()"
#Output: ["(a)()()", "(a())()"]
# 
#
# Example 3: 
#
# 
#Input: ")("
#Output: [""]
# Related Topics Depth-first Search Breadth-first Search



#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        ans = []
        def isValid(s):
            cnt = 0
            for ch in s:
                if ch=='(': cnt+=1
                elif ch==')':
                    cnt-=1
                    if cnt<0: return False
            return cnt==0
        if isValid(s): return [s]
        queue = collections.deque()
        queue.append(s)
        visited = set()
        visited.add(s)
        found = False
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                for i in range(len(node)):
                    if node[i] not in ['(',')']: continue
                    nextNd = node[:i]+node[i+1:]
                    if nextNd not in visited:
                        if isValid(nextNd):
                            ans.append(nextNd)
                            found = True
                        queue.append(nextNd)
                        visited.add(nextNd)
            if found: return ans
        return ans


#leetcode submit region end(Prohibit modification and deletion)
