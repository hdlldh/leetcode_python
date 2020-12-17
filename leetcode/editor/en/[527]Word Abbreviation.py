# Given an array of n distinct non-empty strings, you need to generate minimal p
# ossible abbreviations for every word following rules below. 
# 
#  
#  Begin with the first character and then the number of characters abbreviated,
#  which followed by the last character. 
#  If there are any conflict, that is more than one words share the same abbrevi
# ation, a longer prefix is used instead of only the first character until making 
# the map from word to abbreviation become unique. In other words, a final abbrevi
# ation cannot map to more than one original words. 
#  If the abbreviation doesn't make the word shorter, then keep it as original. 
# 
#  
# 
#  Example: 
#  
# Input: ["like", "god", "internal", "me", "internet", "interval", "intension", 
# "face", "intrusion"]
# Output: ["l2e","god","internal","me","i6t","interval","inte4n","f2e","intr4n"]
# 
#  
#  
# 
# 
# Note: 
#  
#  Both n and the length of each word will not exceed 400. 
#  The length of each word is greater than 1. 
#  The words consist of lowercase English letters only. 
#  The return answers should be in the same order as the original array. 
#  Related Topics String Sort


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def wordsAbbreviation(self, dict):
        """
        :type dict: List[str]
        :rtype: List[str]
        """
        n = len(dict)
        ans = [""]*n
        pre = [1] * n
        for i in range(n):
            ans[i] = self.abbr(dict[i], 1)
        for i in range(n):
            while True:
                st = set()
                for j in range(i+1, n):
                    if ans[i] == ans[j]:
                        st.add(j)
                if not st: break
                st.add(i)
                for j in st:
                    pre[j] += 1
                    ans[j] = self.abbr(dict[j], pre[j])
        return ans

    def abbr(self, s, k):
        n = len(s)
        if k >= n-2: return s
        return s[:k] + str(n-k-1) + s[-1]
        
# leetcode submit region end(Prohibit modification and deletion)
