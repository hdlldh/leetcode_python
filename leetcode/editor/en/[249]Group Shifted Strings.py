#Given a string, we can "shift" each of its letter to its successive letter, for example: "abc" -> "bcd". We can keep "shifting" which forms the sequence: 
#
# 
#"abc" -> "bcd" -> ... -> "xyz" 
#
# Given a list of strings which contains only lowercase alphabets, group all strings that belong to the same shifting sequence. 
#
# Example: 
#
# 
#Input: ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"],
#Output: 
#[
#  ["abc","bcd","xyz"],
#  ["az","ba"],
#  ["acef"],
#  ["a","z"]
#]
# 
# Related Topics Hash Table String



#leetcode submit region begin(Prohibit modification and deletion)
from collections import defaultdict
class Solution(object):
    def groupStrings(self, strings):
        """
        :type strings: List[str]
        :rtype: List[List[str]]
        """
        hmap = defaultdict(list)
        for string in strings:
            sig = ''
            if len(string) > 1:
                for i in range(1, len(string)):
                    sig += str((ord(string[i]) - ord(string[i - 1])) % 26)

            hmap[sig].append(string)
        return hmap.values()
#leetcode submit region end(Prohibit modification and deletion)
