#A string such as "word" contains the following abbreviations: 
#
# ["word", "1ord", "w1rd", "wo1d", "wor1", "2rd", "w2d", "wo2", "1o1d", "1or1", "w1r1", "1o2", "2r1", "3d", "w3", "4"]
# 
#
# Given a target string and a set of strings in a dictionary, find an abbreviation of this target string with the smallest possible length such that it does not conflict with abbreviations of the strings in the dictionary. 
#
# Each number or letter in the abbreviation is considered length = 1. For example, the abbreviation "a32bc" has length = 4. 
#
# Note: 
# 
# In the case of multiple answers as shown in the second example below, you may return any one of them. 
# Assume length of target string = m, and dictionary size = n. You may assume that m ≤ 21, n ≤ 1000, and log2(n) + m ≤ 20. 
# 
# 
#
# Examples: 
# 
#"apple", ["blade"] -> "a4" (because "5" or "4e" conflicts with "blade")
#
#"apple", ["plain", "amber", "blade"] -> "1p3" (other valid answers include "ap3", "a3e", "2p2", "3le", "3l1").
# 
# Related Topics Backtracking Bit Manipulation



#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def minAbbreviation(self, target, dictionary):
        """
        :type target: str
        :type dictionary: List[str]
        :rtype: str
        """
        if not target: return ""
        if not dictionary: return str(len(target))

        n = len(target)
        dictionary = set([d for d in dictionary if len(d)==n])
        pq = []
        for i in range(1 << n):
            cnt = 0
            out = ""
            for j in range(n):
                if (i >> j) & 1:
                    cnt += 1
                else:
                    if cnt > 0:
                        out += str(cnt)
                        cnt = 0
                    out += target[j]
            if cnt > 0: out += str(cnt)
            conflict = False
            for word in dictionary:
                if self.valid(word, out):
                    conflict = True
                    break
            if conflict: continue
            heapq.heappush(pq, [len(out), out])
        if pq: return pq[0][1]
        return ""

    def valid(self, word, abbr):
        m = len(word)
        n = len(abbr)
        i = j = 0
        while i<m and j<n:
            val = 0
            if abbr[j]>='0' and abbr[j] <='9':
                if abbr[j] == '0': return False
                while j<n and abbr[j]>='0' and abbr[j] <='9':
                    val = val *10+ ord(abbr[j]) -ord('0')
                    j+=1
                i += val
            else:
                if abbr[j]!=word[i]: return False
                i+=1
                j+=1
        return i==m and j==n

        
#leetcode submit region end(Prohibit modification and deletion)
