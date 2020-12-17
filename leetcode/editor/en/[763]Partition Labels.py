#
#A string S of lowercase letters is given. We want to partition this string into as many parts as possible so that each letter appears in at most one part, and return a list of integers representing the size of these parts.
# 
#
# Example 1: 
# 
#Input: S = "ababcbacadefegdehijhklij"
#Output: [9,7,8]
#Explanation:
#The partition is "ababcbaca", "defegde", "hijhklij".
#This is a partition so that each letter appears in at most one part.
#A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits S into less parts.
# 
# 
#
# Note: 
# S will have length in range [1, 500]. 
# S will consist of lowercase letters ('a' to 'z') only. 
# Related Topics Two Pointers Greedy



#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        hmap = {}
        intervals = []
        n = 0
        for i, ch in enumerate(S):
            if ch not in hmap:
                hmap[ch] = n
                intervals.append([i, i])
                n += 1
            else:
                intervals[hmap[ch]][1] = i
        ans = []
        i = 0
        j = 1
        while j < n:
            if intervals[j][0] <= intervals[i][1]:
                intervals[i][1] = max(intervals[i][1], intervals[j][1])
            else:
                ans.append(intervals[i][1] - intervals[i][0] + 1)
                i = j
            j += 1
        ans.append(intervals[i][1] - intervals[i][0] + 1)
        return ans

#leetcode submit region end(Prohibit modification and deletion)
