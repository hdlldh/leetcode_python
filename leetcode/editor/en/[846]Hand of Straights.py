# Alice has a hand of cards, given as an array of integers. 
# 
#  Now she wants to rearrange the cards into groups so that each group is size W
# , and consists of W consecutive cards. 
# 
#  Return true if and only if she can. 
# 
#  
# 
#  
#  
# 
#  Example 1: 
# 
#  
# Input: hand = [1,2,3,6,2,3,4,7,8], W = 3
# Output: true
# Explanation: Alice's hand can be rearranged as [1,2,3],[2,3,4],[6,7,8]. 
# 
#  Example 2: 
# 
#  
# Input: hand = [1,2,3,4,5], W = 4
# Output: false
# Explanation: Alice's hand can't be rearranged into groups of 4. 
# 
#  
# 
#  Note: 
# 
#  
#  1 <= hand.length <= 10000 
#  0 <= hand[i] <= 10^9 
#  1 <= W <= hand.length 
#  
#  Related Topics Ordered Map


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def isNStraightHand(self, hand, W):
        """
        :type hand: List[int]
        :type W: int
        :rtype: bool
        """
        N = len(hand)
        count = collections.Counter(hand)
        while count:
            m = min(count)
            v = count[m]
            for k in xrange(m, m+W):
                if count[k]< v: return False
                count[k] -= v
                if count[k] ==0: del count[k]
        return True
# leetcode submit region end(Prohibit modification and deletion)
