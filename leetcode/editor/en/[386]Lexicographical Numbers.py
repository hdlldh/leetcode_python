#Given an integer n, return 1 - n in lexicographical order. 
#
# For example, given 13, return: [1,10,11,12,13,2,3,4,5,6,7,8,9]. 
#
# Please optimize your algorithm to use less time and space. The input size may be as large as 5,000,000. 
#



#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):

    def lexicalOrder2(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        ans = [0]*n
        cur = 1
        for i in range(n):
            ans[i] = cur
            if cur*10<=n:
                cur *= 10
            else:
                if cur>=n: cur = cur//10
                cur += 1
                while cur%10==0: cur = cur//10
        return ans

    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        ans = []
        for i in range(1,10):
            self.dfs(i, n, ans)
        return ans

    def dfs(self, cur, n, ans):
        if cur>n: return
        ans.append(cur)
        for i in range(10):
            self.dfs(cur*10+i, n, ans)

#leetcode submit region end(Prohibit modification and deletion)
