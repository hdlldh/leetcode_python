#Given a string s, return all the palindromic permutations (without duplicates) of it. Return an empty list if no palindromic permutation could be form. 
#
# Example 1: 
#
# 
#Input: "aabb"
#Output: ["abba", "baab"] 
#
# Example 2: 
#
# 
#Input: "abc"
#Output: [] 
# Related Topics Backtracking



#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def generatePalindromes(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        n = len(s)
        counter = collections.Counter(s)
        c = None
        for k, v in counter.items():
            if v%2==1:
                if c is None: c=k
                else: return []

        if c is None: c=""
        ans = []

        def helper(counter, n, out, ans):
            if len(out) == n:
                ans.append(out)
                return

            for k, v in counter.items():
                if v>=2:
                    counter[k] -= 2
                    helper(counter, n, k+out+k, ans)
                    counter[k] += 2

        helper(counter, n, c, ans)
        return ans

        
#leetcode submit region end(Prohibit modification and deletion)
