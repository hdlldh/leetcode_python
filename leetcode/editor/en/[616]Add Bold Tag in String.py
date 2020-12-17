# Given a string s and a list of strings dict, you need to add a closed pair of 
# bold tag <b> and </b> to wrap the substrings in s that exist in dict. If two suc
# h substrings overlap, you need to wrap them together by only one pair of closed 
# bold tag. Also, if two substrings wrapped by bold tags are consecutive, you need
#  to combine them. 
# 
#  Example 1: 
#  
# Input: 
# s = "abcxyz123"
# dict = ["abc","123"]
# Output:
# "<b>abc</b>xyz<b>123</b>"
#  
#  
# 
#  Example 2: 
#  
# Input: 
# s = "aaabbcc"
# dict = ["aaa","aab","bc"]
# Output:
# "<b>aaabbc</b>c"
#  
#  
# 
#  Note: 
#  
#  The given dict won't contain duplicates, and its length won't exceed 100. 
#  All the strings in input have length in range [1, 1000]. 
#  
#  Related Topics String


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def addBoldTag(self, s, dict):
        """
        :type s: str
        :type dict: List[str]
        :rtype: str
        """
        if not dict: return s
        wordset = set()
        minLen = float('inf')
        maxLen = -float('inf')
        for word in dict:
            wordset.add(word)
            minLen = min(minLen, len(word))
            maxLen = max(maxLen, len(word))

        n = len(s)
        intervals = []

        def insert_interval(intervals, start, end):
            l = []
            r = []
            for i in range(len(intervals)):
                if intervals[i][0] > end:
                    r.append(intervals[i])
                elif intervals[i][1] < start:
                    l.append(intervals[i])
                else:
                    start = min(start, intervals[i][0])
                    end = max(end, intervals[i][1])
            return l + [[start, end]] + r

        for i in range(n):
            for l in range(minLen, maxLen + 1):
                if i + l > n: continue
                if s[i:i + l] in wordset:
                    intervals = insert_interval(intervals, i, i + l)

        prev = 0
        ans = ""
        for i in range(len(intervals)):
            ans += s[prev:intervals[i][0]]
            ans += '<b>%s</b>' % s[intervals[i][0]:intervals[i][1]]
            prev = intervals[i][1]
        ans += s[prev:]
        return ans
        
# leetcode submit region end(Prohibit modification and deletion)
