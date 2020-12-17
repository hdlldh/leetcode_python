#A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down). 
#
# Find all strobogrammatic numbers that are of length = n. 
#
# Example: 
#
# 
#Input:  n = 2
#Output: ["11","69","88","96"]
# 
# Related Topics Math Recursion



#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def findStrobogrammatic(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n==1: return ['0','1','8']
        n1 = n//2

        def dfs(start, n, out, ans):
            if start == n:
                ans.append(out)
                return
            for num in ['0','1','6','8','9']:
                if start==0 and num=='0': continue
                dfs(start + 1, n, out+num, ans)

        ans = []
        dfs(0, n1, '', ans)
        ans1 =[]
        for num in ans:
            if n%2:
                ans1.append(num + '0' + self.get_another(num))
                ans1.append(num + '1' + self.get_another(num))
                ans1.append(num + '8' + self.get_another(num))
            else:
                ans1.append(num + self.get_another(num))
        return ans1

    def get_another(self, num):
        mem = {'6': '9', '9': '6', '8': '8', '1': '1', '0': '0'}
        n = len(num)
        t = ''
        for i in range(n-1, -1, -1):
            t += mem[num[i]]
        return t



        
#leetcode submit region end(Prohibit modification and deletion)
