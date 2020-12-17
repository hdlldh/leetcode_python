#You are given a string, s, and a list of words, words, that are all of the same length. Find all starting indices of substring(s) in s that is a concatenation of each word in words exactly once and without any intervening characters. 
#
# Example 1: 
#
# 
#Input:
#  s = "barfoothefoobarman",
#  words = ["foo","bar"]
#Output: [0,9]
#Explanation: Substrings starting at index 0 and 9 are "barfoor" and "foobar" respectively.
#The output order does not matter, returning [9,0] is fine too.
# 
#
# Example 2: 
#
# 
#Input:
#  s = "wordgoodgoodgoodbestword",
#  words = ["word","good","best","word"]
#Output: []
# 
# Related Topics Hash Table Two Pointers String



#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        n = len(s)
        if n == 0: return []
        wordNum = len(words)
        if wordNum == 0: return []
        wordLen = len(words[0])

        ans = []
        ref = {}
        for word in words:
            ref[word] = ref.get(word, 0) + 1

        for i in range(wordLen):
            hmap = {}
            k = i
            if k + wordNum * wordLen <= n:
                for j in range(wordNum):
                    word = s[k + j * wordLen:k + (j + 1) * wordLen]
                    hmap[word] = hmap.get(word, 0) + 1
                if hmap == ref: ans.append(k)
            while k + (wordNum + 1) * wordLen <= n:
                word = s[k:k + wordLen]
                if hmap[word] == 1:
                    del hmap[word]
                else:
                    hmap[word] -= 1
                word = s[k + wordNum * wordLen:k + (wordNum + 1) * wordLen]
                hmap[word] = hmap.get(word, 0) + 1
                k += wordLen
                if hmap == ref: ans.append(k)
        return ans




        
#leetcode submit region end(Prohibit modification and deletion)
