#Write a function to generate the generalized abbreviations of a word. 
#
# Note: The order of the output does not matter. 
#
# Example: 
#
# 
#Input: "word"
#Output:
#["word", "1ord", "w1rd", "wo1d", "wor1", "2rd", "w2d", "wo2", "1o1d", "1or1", "w1r1", "1o2", "2r1", "3d", "w3", "4"]
# 
#
# 
# Related Topics Backtracking Bit Manipulation



#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def generateAbbreviations(self, word):
        """
        :type word: str
        :rtype: List[str]
        """
        n = len(word)
        ans = []
        for i in range(1<<n):
            out = ""
            cnt = 0
            for j in range(n):
                if (i>>j) & 1: cnt +=1
                else:
                    if cnt>0:
                        out += str(cnt)
                        cnt = 0
                    out += word[j]
            if cnt > 0: out += str(cnt)
            ans.append(out)
        return ans
        
#leetcode submit region end(Prohibit modification and deletion)
