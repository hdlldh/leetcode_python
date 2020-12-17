#Given a string containing only digits, restore it by returning all possible valid IP address combinations. 
#
# Example: 
#
# 
#Input: "25525511135"
#Output: ["255.255.11.135", "255.255.111.35"]
# 
# Related Topics String Backtracking



#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        ans = []
        self.dfs(s,0,0,"",ans)
        return ans

    def dfs(self, s, start, id, out, ans):
        if start>=len(s): return
        if id==3:
            num = s[start:]
            if len(num)>1 and num[0]=='0': return
            if len(num)>4 or int(num)>255: return
            ans.append(out+num)
        else:
            for k in range(1,4):
                if start+k>=len(s): continue
                num = s[start:start+k]
                if len(num) > 1 and num[0] == '0': continue
                if int(num) > 255: continue
                self.dfs(s,start+k, id+1, out+num+'.', ans)

#leetcode submit region end(Prohibit modification and deletion)
