# Given a list of strings, you could concatenate these strings together into a l
# oop, where for each string you could choose to reverse it or not. Among all the 
# possible loops, you need to find the lexicographically biggest string after cutt
# ing the loop, which will make the looped string into a regular one. 
# 
#  Specifically, to find the lexicographically biggest string, you need to exper
# ience two phases: 
#  
#  Concatenate all the strings into a loop, where you can reverse some strings o
# r not and connect them in the same order as given. 
#  Cut and make one breakpoint in any place of the loop, which will make the loo
# ped string into a regular one starting from the character at the cutpoint. 
#  
#  
# 
#  And your job is to find the lexicographically biggest one among all the possi
# ble regular strings. 
# 
# 
#  Example: 
#  
# Input: "abc", "xyz"
# Output: "zyxcba"
# Explanation: You can get the looped string "-abcxyz-", "-abczyx-", "-cbaxyz-",
#  "-cbazyx-", where '-' represents the looped status. The answer string came from
#  the fourth looped one, where you could cut from the middle character 'a' and ge
# t "zyxcba".
#  
#  
# 
#  Note: 
#  
#  The input strings will only contain lowercase letters. 
#  The total length of all the strings will not over 1,000. 
#  
#  Related Topics String


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def splitLoopedString(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        s = ""

        n = len(strs)
        for i, org in enumerate(strs):
            rev = org[::-1]
            if rev > org:
                s += rev
            else:
                s += org
        res = s
        cur = 0
        for i in range(n):
            org = strs[i]
            rev = org[::-1]
            l = len(org)
            part1 = s[:cur]
            part2 = s[cur + l:]
            for j in range(l):
                org1 = org[:j]
                org2 = org[j:]
                rev1 = rev[:j]
                rev2 = rev[j:]
                if org2 + part2 + part1 + org1 > res:
                    res = org2 + part2 + part1 + org1
                if rev2 + part2 + part1 + rev1 > res:
                    res = rev2 + part2 + part1 + rev1
            cur += len(org)
        return res
        
# leetcode submit region end(Prohibit modification and deletion)
