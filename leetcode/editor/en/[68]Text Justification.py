#Given an array of words and a width maxWidth, format the text such that each line has exactly maxWidth characters and is fully (left and right) justified. 
#
# You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters. 
#
# Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line do not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right. 
#
# For the last line of text, it should be left justified and no extra space is inserted between words. 
#
# Note: 
#
# 
# A word is defined as a character sequence consisting of non-space characters only. 
# Each word's length is guaranteed to be greater than 0 and not exceed maxWidth. 
# The input array words contains at least one word. 
# 
#
# Example 1: 
#
# 
#Input:
#words = ["This", "is", "an", "example", "of", "text", "justification."]
#maxWidth = 16
#Output:
#[
#   "This    is    an",
#   "example  of text",
#   "justification.  "
#]
# 
#
# Example 2: 
#
# 
#Input:
#words = ["What","must","be","acknowledgment","shall","be"]
#maxWidth = 16
#Output:
#[
#  "What   must   be",
#  "acknowledgment  ",
#  "shall be        "
#]
#Explanation: Note that the last line is "shall be    " instead of "shall     be",
#             because the last line must be left-justified instead of fully-justified.
#             Note that the second line is also left-justified becase it contains only one word.
# 
#
# Example 3: 
#
# 
#Input:
#words = ["Science","is","what","we","understand","well","enough","to","explain",
#         "to","a","computer.","Art","is","everything","else","we","do"]
#maxWidth = 20
#Output:
#[
#  "Science  is  what we",
#  "understand      well",
#  "enough to explain to",
#  "a  computer.  Art is",
#  "everything  else  we",
#  "do                  "
#]
# 
# Related Topics String



#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        ans = []
        t = []
        chCnt = 0
        for word in words:
            if chCnt + len(t) + len(word) <= maxWidth:
                t.append(word)
                chCnt += len(word)
            else:
                spaces = maxWidth - chCnt
                n = len(t)
                if n == 1:
                    t[0] += ' ' * spaces
                else:
                    for i in range(spaces):
                        t[i % (n - 1)] += ' '
                ans.append(''.join(t))
                t = [word]
                chCnt = len(word)

        last = ' '.join(t)
        last += ' ' * (maxWidth - len(last))
        ans.append(last)
        return ans
        
#leetcode submit region end(Prohibit modification and deletion)
