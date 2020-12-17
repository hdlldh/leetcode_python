#The set [1,2,3,...,n] contains a total of n! unique permutations. 
#
# By listing and labeling all of the permutations in order, we get the following sequence for n = 3: 
#
# 
# "123" 
# "132" 
# "213" 
# "231" 
# "312" 
# "321" 
# 
#
# Given n and k, return the kth permutation sequence. 
#
# Note: 
#
# 
# Given n will be between 1 and 9 inclusive. 
# Given k will be between 1 and n! inclusive. 
# 
#
# Example 1: 
#
# 
#Input: n = 3, k = 3
#Output: "213"
# 
#
# Example 2: 
#
# 
#Input: n = 4, k = 9
#Output: "2314"
# 
# Related Topics Math Backtracking



#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def getPermutation2(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        visited = [0] * n
        self.ans = None
        self.count = 0

        def dfs(n, k, out, visited):
            if len(out) == n:
                self.count += 1
                if self.count == k:
                    self.ans = ''.join([str(num) for num in out])
                    return True
                return False
            for i in range(1, n+1):
                if visited[i-1] == 1: continue
                visited[i-1] = 1
                if dfs(n, k, out+[i], visited): return True
                visited[i-1] = 0
            return False

        dfs(n, k, [], visited)
        return self.ans

    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        candidates = [n for n in range(1, n + 1)]
        ans = ""
        num = 1
        for i in range(1, n):
            num *= i
        for i in range(n):
            j = int((k - 1) // num)
            ans += str(candidates[j])
            candidates.pop(j)
            k = k % num
            if n > i + 1:
                num = num / (n - i - 1)
        return ans


#leetcode submit region end(Prohibit modification and deletion)
