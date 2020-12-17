#You are playing the following Flip Game with your friend: Given a string that contains only these two characters: + and -, you and your friend take turns to flip two consecutive "++" into "--". The game ends when a person can no longer make a move and therefore the other person will be the winner. 
#
# Write a function to determine if the starting player can guarantee a win. 
#
# Example: 
#
# 
#Input: s = "++++"
#Output: true 
#Explanation: The starting player can guarantee a win by flipping the middle "++" to become "+--+".
# 
#
# Follow up: 
#Derive your algorithm's runtime complexity. Related Topics Backtracking Minimax



#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def canWin(self, s):
        """
        :type s: str
        :rtype: bool
        """
        n = len(s)
        for i in range(1, n):
            if s[i] == '+' and s[i - 1] == '+':
                t = s[:i - 1] + '--' + s[i + 1:]
                if not self.canWin(t): return True
        return False
        
#leetcode submit region end(Prohibit modification and deletion)
