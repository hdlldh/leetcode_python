#An abbreviation of a word follows the form <first letter><number><last letter>. Below are some examples of word abbreviations: 
#
# 
#a) it                      --> it    (no abbreviation)
#
#     1
#     ↓
#b) d|o|g                   --> d1g
#
#              1    1  1
#     1---5----0----5--8
#     ↓   ↓    ↓    ↓  ↓    
#c) i|nternationalizatio|n  --> i18n
#
#              1
#     1---5----0
#     ↓   ↓    ↓
#d) l|ocalizatio|n          --> l10n
# 
#
# Assume you have a dictionary and given a word, find whether its abbreviation is unique in the dictionary. A word's abbreviation is unique if no other word from the dictionary has the same abbreviation. 
#
# Example: 
#
# 
#Given dictionary = [ "deer", "door", "cake", "card" ]
#
#isUnique("dear") -> false
#isUnique("cart") -> true
#isUnique("cane") -> false
#isUnique("make") -> true
# 
# Related Topics Hash Table Design



#leetcode submit region begin(Prohibit modification and deletion)
class ValidWordAbbr(object):

    def __init__(self, dictionary):
        """
        :type dictionary: List[str]
        """
        self.counter = collections.defaultdict(set)
        for word in dictionary:
            abbr = self.get_abbr(word)
            self.counter[abbr].add(word)

    def isUnique(self, word):
        """
        :type word: str
        :rtype: bool
        """
        abbr = self.get_abbr(word)
        if abbr not in self.counter: return True
        if word in self.counter[abbr] and len(self.counter[abbr])==1: return True
        return False


    def get_abbr(self, word):
        """
        :type word: str
        :rtype: bool
        """
        l = len(word)
        if l<=2: return word
        return word[0]+ str(l-2)+word[-1]


# Your ValidWordAbbr object will be instantiated and called as such:
# obj = ValidWordAbbr(dictionary)
# param_1 = obj.isUnique(word)
#leetcode submit region end(Prohibit modification and deletion)
