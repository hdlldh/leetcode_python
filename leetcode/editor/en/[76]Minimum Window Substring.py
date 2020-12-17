#Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n). 
#
# Example: 
#
# 
#Input: S = "ADOBECODEBANC", T = "ABC"
#Output: "BANC"
# 
#
# Note: 
#
# 
# If there is no such window in S that covers all characters in T, return the empty string "". 
# If there is such window, you are guaranteed that there will always be only one unique minimum window in S. 
# 
# Related Topics Hash Table Two Pointers String Sliding Window



#leetcode submit region begin(Prohibit modification and deletion)

class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        count = collections.Counter(t)
        left = 0
        n = len(s)
        cnt = 0
        ans = ""
        minLen = float('inf')
        for i in range(n):
            count[s[i]] -= 1
            if count[s[i]] >= 0: cnt += 1
            while cnt == len(t):
                if i - left + 1 < minLen:
                    minLen = i - left + 1
                    ans = s[left:i + 1]
                count[s[left]] += 1
                if count[s[left]] > 0: cnt -= 1
                left += 1
        return ans

    def minWindow2(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        count = collections.Counter(t)
        data = collections.Counter()

        minSize = float('inf')
        ans = ""

        pos = [i for i in range(len(s)) if s[i] in count]
        left = 0
        for i in range(len(pos)):
            data[s[pos[i]]]+=1
            while self.check(data, count):
                size = pos[i] - pos[left] + 1
                if size < minSize:
                    minSize = size
                    ans = s[pos[left]:pos[i] + 1]
                data[s[pos[left]]] -=1
                left += 1
        return ans


    def check(self, data, target):
        for k, v in target.items():
            if data[k]<v: return False
        return True
#leetcode submit region end(Prohibit modification and deletion)
