# In an alien language, surprisingly they also use english lowercase letters, bu
# t possibly in a different order. The order of the alphabet is some permutation o
# f lowercase letters. 
# 
#  Given a sequence of words written in the alien language, and the order of the
#  alphabet, return true if and only if the given words are sorted lexicographical
# y in this alien language. 
#  
#  Example 1: 
# 
#  
# Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
# Output: true
# Explanation: As 'h' comes before 'l' in this language, then the sequence is so
# rted.
#  
# 
#  Example 2: 
# 
#  
# Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
# Output: false
# Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1]
# , hence the sequence is unsorted.
#  
# 
#  Example 3: 
# 
#  
# Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
# Output: false
# Explanation: The first three characters "app" match, and the second string is 
# shorter (in size.) According to lexicographical rules "apple" > "app", because '
# l' > '∅', where '∅' is defined as the blank character which is less than any oth
# er character (More info).
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= words.length <= 100 
#  1 <= words[i].length <= 20 
#  order.length == 26 
#  All characters in words[i] and order are English lowercase letters. 
#  
#  Related Topics Hash Table


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        dictionary = {}
        for i, ch in enumerate(order):
            dictionary[ch] = i

        sorted_words = sorted(words, key=lambda x: [dictionary[ch] for ch in x])

        N = len(words)
        for i in range(N):
            if words[i]!=sorted_words[i]:return False
        return True

        
# leetcode submit region end(Prohibit modification and deletion)
