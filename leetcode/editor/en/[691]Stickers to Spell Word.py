# 
# We are given N different types of stickers. Each sticker has a lowercase Engli
# sh word on it.
#  
# You would like to spell out the given target string by cutting individual lett
# ers from your collection of stickers and rearranging them.
#  
# You can use each sticker more than once if you want, and you have infinite qua
# ntities of each sticker.
#  
# What is the minimum number of stickers that you need to spell out the target? 
# If the task is impossible, return -1.
#  
# 
#  Example 1: 
#  Input: 
# ["with", "example", "science"], "thehat"
#  
# 
#  Output: 
# 3
#  
# 
#  Explanation: 
# We can use 2 "with" stickers, and 1 "example" sticker.
# After cutting and rearrange the letters of those stickers, we can form the tar
# get "thehat".
# Also, this is the minimum number of stickers necessary to form the target stri
# ng.
#  
# 
#  Example 2: 
#  Input: 
# ["notice", "possible"], "basicbasic"
#  
# 
#  Output: 
# -1
#  
# 
#  Explanation: 
# We can't form the target "basicbasic" from cutting letters from the given stic
# kers.
#  
# 
#  Note:
#  stickers has length in the range [1, 50]. 
#  stickers consists of lowercase English words (without apostrophes). 
#  target has length in the range [1, 15], and consists of lowercase English let
# ters. 
#  In all test cases, all words were chosen randomly from the 1000 most common U
# S English words, and the target was chosen as a concatenation of two random word
# s. 
#  The time limit may be more challenging than usual. It is expected that a 50 s
# ticker test case can be solved within 35ms on average. 
#  Related Topics Dynamic Programming Backtracking


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def minStickers(self, stickers, target):
        """
        :type stickers: List[str]
        :type target: str
        :rtype: int
        """
        n = len(stickers)
        m = len(target)
        states = [[0] * 26 for _ in range(n)]
        for i in range(n):
            for ch in stickers[i]:
                states[i][ord(ch) - ord('a')] += 1

        dest = (1 << m) - 1
        queue = collections.deque()
        queue.append(0)
        visited = set()
        visited.add(0)

        steps = 0
        while queue:
            size = len(queue)
            for _ in range(size):
                cur = queue.popleft()
                if cur == dest: return steps
                for i in range(n):
                    tmp = states[i][:]
                    nxt = cur
                    for j in range(m):
                        if (cur & (1 << j)) == 0 and tmp[ord(target[j]) - ord('a')] > 0:
                            nxt |= (1 << j)
                            tmp[ord(target[j]) - ord('a')] -= 1
                    if nxt in visited: continue
                    queue.append(nxt)
                    visited.add(nxt)
            steps += 1
        return -1
        
# leetcode submit region end(Prohibit modification and deletion)
