# We are given two sentences A and B. (A sentence is a string of space separated
#  words. Each word consists only of lowercase letters.) 
# 
#  A word is uncommon if it appears exactly once in one of the sentences, and do
# es not appear in the other sentence. 
# 
#  Return a list of all uncommon words. 
# 
#  You may return the list in any order. 
# 
#  
# 
#  
#  
# 
#  
#  Example 1: 
# 
#  
# Input: A = "this apple is sweet", B = "this apple is sour"
# Output: ["sweet","sour"]
#  
# 
#  
#  Example 2: 
# 
#  
# Input: A = "apple apple", B = "banana"
# Output: ["banana"]
#  
# 
#  
# 
#  Note: 
# 
#  
#  0 <= A.length <= 200 
#  0 <= B.length <= 200 
#  A and B both contain only spaces and lowercase letters. 
#  
#  
#  
#  Related Topics Hash Table


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        
# leetcode submit region end(Prohibit modification and deletion)
