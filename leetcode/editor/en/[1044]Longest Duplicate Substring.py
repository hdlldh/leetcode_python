# Given a string S, consider all duplicated substrings: (contiguous) substrings 
# of S that occur 2 or more times. (The occurrences may overlap.) 
# 
#  Return any duplicated substring that has the longest possible length. (If S d
# oes not have a duplicated substring, the answer is "".) 
# 
#  
# 
#  Example 1: 
# 
#  
# Input: "banana"
# Output: "ana"
#  
# 
#  Example 2: 
# 
#  
# Input: "abcd"
# Output: ""
#  
# 
#  
# 
#  Note: 
# 
#  
#  2 <= S.length <= 10^5 
#  S consists of lowercase English letters. 
#  
#  Related Topics Hash Table Binary Search


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def longestDupSubstring(self, S):
        """
        :type S: str
        :rtype: str
        """
        n = len(S)
        low = 1
        high = n

        def get_duplicate(L):
            h = 0
            module = 2 ** 32
            a = 26
            for i in xrange(L):
                h = (h * a + ord(S[i]) - ord('a')) % module

            mem = set()
            mem.add(h)
            aL = pow(a, L) % module
            for i in xrange(L, n):
                h = (h * a - aL * (ord(S[i - L]) - ord('a')) + ord(S[i]) - ord('a')) % module
                # h = (h+module) % module
                if h in mem: return S[i - L + 1:i + 1]
                mem.add(h)
            return ""

        while low <= high:
            mid = low + (high - low) // 2
            dup_str = get_duplicate(mid)
            if not dup_str:
                high = mid - 1
            else:
                low = mid + 1

        if high == 0: return ""
        return get_duplicate(high)
        
# leetcode submit region end(Prohibit modification and deletion)
