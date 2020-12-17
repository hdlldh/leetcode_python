# Given a paragraph and a list of banned words, return the most frequent word th
# at is not in the list of banned words. It is guaranteed there is at least one wo
# rd that isn't banned, and that the answer is unique. 
# 
#  Words in the list of banned words are given in lowercase, and free of punctua
# tion. Words in the paragraph are not case sensitive. The answer is in lowercase.
#  
# 
#  
# 
#  Example: 
# 
#  
# Input: 
# paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
# banned = ["hit"]
# Output: "ball"
# Explanation: 
# "hit" occurs 3 times, but it is a banned word.
# "ball" occurs twice (and no other word does), so it is the most frequent non-b
# anned word in the paragraph. 
# Note that words in the paragraph are not case sensitive,
# that punctuation is ignored (even if adjacent to words, such as "ball,"), 
# and that "hit" isn't the answer even though it occurs more because it is banne
# d.
#  
# 
#  
# 
#  Note: 
# 
#  
#  1 <= paragraph.length <= 1000. 
#  0 <= banned.length <= 100. 
#  1 <= banned[i].length <= 10. 
#  The answer is unique, and written in lowercase (even if its occurrences in pa
# ragraph may have uppercase symbols, and even if it is a proper noun.) 
#  paragraph only consists of letters, spaces, or the punctuation symbols !?',;.
#  
#  There are no hyphens or hyphenated words. 
#  Words only consist of letters, never apostrophes or other punctuation symbols
# . 
#  
#  Related Topics String


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        banned_set = set(banned)
        n = len(paragraph)
        i = 0
        count = collections.Counter()
        while i<n and not paragraph[i].isalpha(): i+=1
        left = i
        while i<n:
            if paragraph[i].isalpha():
                i+=1
                if i!=n:continue
            word = paragraph[left:i].lower()
            if word not in banned_set:
                count[word] += 1
            while i < n and not paragraph[i].isalpha(): i += 1
            left = i
        if count: return count.most_common(1)[0][0]
        return ""

        
# leetcode submit region end(Prohibit modification and deletion)
