# A gene string can be represented by an 8-character long string, with choices f
# rom "A", "C", "G", "T". 
# 
#  Suppose we need to investigate about a mutation (mutation from "start" to "en
# d"), where ONE mutation is defined as ONE single character changed in the gene s
# tring. 
# 
#  For example, "AACCGGTT" -> "AACCGGTA" is 1 mutation. 
# 
#  Also, there is a given gene "bank", which records all the valid gene mutation
# s. A gene must be in the bank to make it a valid gene string. 
# 
#  Now, given 3 things - start, end, bank, your task is to determine what is the
#  minimum number of mutations needed to mutate from "start" to "end". If there is
#  no such a mutation, return -1. 
# 
#  Note: 
# 
#  
#  Starting point is assumed to be valid, so it might not be included in the ban
# k. 
#  If multiple mutations are needed, all mutations during in the sequence must b
# e valid. 
#  You may assume start and end string is not the same. 
#  
# 
#  
# 
#  Example 1: 
# 
#  
# start: "AACCGGTT"
# end:   "AACCGGTA"
# bank: ["AACCGGTA"]
# 
# return: 1
#  
# 
#  
# 
#  Example 2: 
# 
#  
# start: "AACCGGTT"
# end:   "AAACGGTA"
# bank: ["AACCGGTA", "AACCGCTA", "AAACGGTA"]
# 
# return: 2
#  
# 
#  
# 
#  Example 3: 
# 
#  
# start: "AAAAACCC"
# end:   "AACCCCCC"
# bank: ["AAAACCCC", "AAACCCCC", "AACCCCCC"]
# 
# return: 3
#  
# 
#  
# 


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def minMutation(self, start, end, bank):
        """
        :type start: str
        :type end: str
        :type bank: List[str]
        :rtype: int
        """
        bankset = set(bank)
        queue = collections.deque()
        queue.append(start)
        visited = set()
        visited.add(start)
        steps = 0
        while queue:
            size = len(queue)
            for _ in range(size):
                cur = queue.popleft()
                if cur == end: return steps
                for i in range(8):
                    for ch in ['A','C','G','T']:
                        nxt = cur[:i]+ch+cur[i+1:]
                        if nxt in visited or nxt not in bankset: continue
                        queue.append(nxt)
                        visited.add(nxt)
            steps += 1
        return -1
        
# leetcode submit region end(Prohibit modification and deletion)
