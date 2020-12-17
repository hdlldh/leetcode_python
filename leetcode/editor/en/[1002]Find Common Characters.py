# Given an array A of strings made only from lowercase letters, return a list of
#  all characters that show up in all strings within the list (including duplicate
# s). For example, if a character occurs 3 times in all strings but not 4 times, y
# ou need to include that character three times in the final answer. 
# 
#  You may return the answer in any order. 
# 
#  
# 
#  
#  Example 1: 
# 
#  
# Input: ["bella","label","roller"]
# Output: ["e","l","l"]
#  
# 
#  
#  Example 2: 
# 
#  
# Input: ["cool","lock","cook"]
# Output: ["c","o"]
#  
# 
#  
# 
#  Note: 
# 
#  
#  1 <= A.length <= 100 
#  1 <= A[i].length <= 100 
#  A[i][j] is a lowercase letter 
#  
#  
#  Related Topics Array Hash Table


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def commonChars(self, A):
        """
        :type A: List[str]
        :rtype: List[str]
        """
        n = len(A)
        if n == 1: return list(A[0])
        counter = collections.Counter(A[0])
        for i in range(1, n):
            counter2 = collections.Counter(A[i])
            for k in counter.keys():
                counter[k] = min(counter[k], counter2[k])

        ans = ""
        for k, v in counter.items():
            if v > 0:
                ans += k * v
        return list(ans)
        
# leetcode submit region end(Prohibit modification and deletion)
