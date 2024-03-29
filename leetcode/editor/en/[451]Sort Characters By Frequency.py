#Given a string, sort it in decreasing order based on the frequency of characters. 
#
# Example 1:
# 
#Input:
#"tree"
#
#Output:
#"eert"
#
#Explanation:
#'e' appears twice while 'r' and 't' both appear once.
#So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
# 
# 
#
# Example 2:
# 
#Input:
#"cccaaa"
#
#Output:
#"cccaaa"
#
#Explanation:
#Both 'c' and 'a' appear three times, so "aaaccc" is also a valid answer.
#Note that "cacaca" is incorrect, as the same characters must be together.
# 
# 
#
# Example 3:
# 
#Input:
#"Aabb"
#
#Output:
#"bbAa"
#
#Explanation:
#"bbaA" is also a valid answer, but "Aabb" is incorrect.
#Note that 'A' and 'a' are treated as two different characters.
# 
# Related Topics Hash Table Heap



#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        pq = []
        counter = collections.Counter(s)
        for k, v in counter.items():
            heapq.heappush(pq, [-v, k])
        ans = ""
        while pq:
            v, k = heapq.heappop(pq)
            ans += k*(-v)
        return ans
#leetcode submit region end(Prohibit modification and deletion)
