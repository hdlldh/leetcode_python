#Given an array of strings, group anagrams together. 
#
# Example: 
#
# 
#Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
#Output:
#[
#  ["ate","eat","tea"],
#  ["nat","tan"],
#  ["bat"]
#] 
#
# Note: 
#
# 
# All inputs will be in lowercase. 
# The order of your output does not matter. 
# 
# Related Topics Hash Table String


import collections
#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        hmap = collections.defaultdict(list)
        for string in strs:
            sig = self.getSignature(string)
            hmap[sig].append(string)
        ans = []
        for val in hmap.values():
            ans.append(val)
        return ans

    def getSignature(self, string):
        sig = [0]*26
        for ch in string:
            sig[ord(ch)-ord('a')] += 1
        return '_'.join([str(n) for n in sig])
#leetcode submit region end(Prohibit modification and deletion)
