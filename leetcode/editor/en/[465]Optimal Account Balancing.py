# A group of friends went on holiday and sometimes lent each other money. For ex
# ample, Alice paid for Bill's lunch for $10. Then later Chris gave Alice $5 for a
#  taxi ride. We can model each transaction as a tuple (x, y, z) which means perso
# n x gave person y $z. Assuming Alice, Bill, and Chris are person 0, 1, and 2 res
# pectively (0, 1, 2 are the person's ID), the transactions can be represented as 
# [[0, 1, 10], [2, 0, 5]]. 
# 
#  Given a list of transactions between a group of people, return the minimum nu
# mber of transactions required to settle the debt. 
# 
#  Note:
#  
#  A transaction will be given as a tuple (x, y, z). Note that x ≠ y and z > 0. 
# 
#  Person's IDs may not be linear, e.g. we could have the persons 0, 1, 2 or we 
# could also have the persons 0, 2, 6. 
#  
#  
# 
#  Example 1:
#  
# Input:
# [[0,1,10], [2,0,5]]
# 
# Output:
# 2
# 
# Explanation:
# Person #0 gave person #1 $10.
# Person #2 gave person #0 $5.
# 
# Two transactions are needed. One way to settle the debt is person #1 pays pers
# on #0 and #2 $5 each.
#  
#  
# 
#  Example 2:
#  
# Input:
# [[0,1,10], [1,0,1], [1,2,5], [2,0,5]]
# 
# Output:
# 1
# 
# Explanation:
# Person #0 gave person #1 $10.
# Person #1 gave person #0 $1.
# Person #1 gave person #2 $5.
# Person #2 gave person #0 $5.
# 
# Therefore, person #1 only need to give person #0 $4, and all debt is settled.
#  
# 


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def minTransfers(self, transactions):
        """
        :type transactions: List[List[int]]
        :rtype: int
        """
        bal = collections.defaultdict(int)
        for u, v, b in transactions:
            bal[u] -= b
            bal[v] += b

        acc = []
        for c, b in bal.items():
            if b != 0: acc.append(c)

        self.ans = float('inf')
        self.helper(acc, bal, 0, 0)
        return self.ans

    def helper(self, acc, bal, start, cnt):
        n = len(acc)
        while start < n and bal[acc[start]] == 0: start += 1
        if start == n:
            print(cnt)
            self.ans = min(self.ans, cnt)
            return

        for i in range(start + 1, n):
            if bal[acc[start]] * bal[acc[i]] < 0:
                bal[acc[i]] += bal[acc[start]]
                self.helper(acc, bal, start + 1, cnt + 1)
                bal[acc[i]] -= bal[acc[start]]
        
# leetcode submit region end(Prohibit modification and deletion)
