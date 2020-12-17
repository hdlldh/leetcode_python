# You are given an array of strings words and a string chars. 
# 
#  A string is good if it can be formed by characters from chars (each character
#  can only be used once). 
# 
#  Return the sum of lengths of all good strings in words. 
# 
#  
# 
#  Example 1: 
# 
#  
# Input: words = ["cat","bt","hat","tree"], chars = "atach"
# Output: 6
# Explanation: 
# The strings that can be formed are "cat" and "hat" so the answer is 3 + 3 = 6.
# 
#  
# 
#  Example 2: 
# 
#  
# Input: words = ["hello","world","leetcode"], chars = "welldonehoneyr"
# Output: 10
# Explanation: 
# The strings that can be formed are "hello" and "world" so the answer is 5 + 5 
# = 10.
#  
# 
#  
# 
#  Note: 
# 
#  
#  1 <= words.length <= 1000 
#  1 <= words[i].length, chars.length <= 100 
#  All strings contain lowercase English letters only. 
#  Related Topics Array Hash Table


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def countCharacters(self, words, chars):
        """
        :type words: List[str]
        :type chars: str
        :rtype: int
        """
        count = collections.Counter(chars)
        ans = 0
        for word in words:
            count1 = collections.Counter(word)
            check = True
            for k, v in count1.items():
                if v>count[k]:
                    check = False
                    break
            if check: ans += len(word)
        return ans
        
# leetcode submit region end(Prohibit modification and deletion)
