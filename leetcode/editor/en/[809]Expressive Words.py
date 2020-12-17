#Sometimes people repeat letters to represent extra feeling, such as "hello" -> "heeellooo", "hi" -> "hiiii". In these strings like "heeellooo", we have groups of adjacent letters that are all the same: "h", "eee", "ll", "ooo". 
#
# For some given string S, a query word is stretchy if it can be made to be equal to S by any number of applications of the following extension operation: choose a group consisting of characters c, and add some number of characters c to the group so that the size of the group is 3 or more. 
#
# For example, starting with "hello", we could do an extension on the group "o" to get "hellooo", but we cannot get "helloo" since the group "oo" has size less than 3. Also, we could do another extension like "ll" -> "lllll" to get "helllllooo". If S = "helllllooo", then the query word "hello" would be stretchy because of these two extension operations: query = "hello" -> "hellooo" -> "helllllooo" = S. 
#
# Given a list of query words, return the number of words that are stretchy. 
#
# 
#
# 
#Example:
#Input: 
#S = "heeellooo"
#words = ["hello", "hi", "helo"]
#Output: 1
#Explanation: 
#We can extend "e" and "o" in the word "hello" to get "heeellooo".
#We can't extend "helo" to get "heeellooo" because the group "ll" is not size 3 or more.
# 
#
# 
#
# Notes: 
#
# 
# 0 <= len(S) <= 100. 
# 0 <= len(words) <= 100. 
# 0 <= len(words[i]) <= 100. 
# S and all words in words consist only of lowercase letters 
# 
#
# 
# Related Topics String



#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def expressiveWords(self, S, words):
        """
        :type S: str
        :type words: List[str]
        :rtype: int
        """

        def stats(word):
            key = []
            val = []
            start = 0
            for i, ch in enumerate(word):
                if i>0 and ch!=word[i-1]:
                    key.append(word[i-1])
                    val.append(i-start)
                    start = i
            key.append(word[-1])
            val.append(len(word)-start)
            return (key, val)
        ans = 0
        keyS, valS = stats(S)
        for word in words:
            keyW, valW = stats(word)
            if keyW!=keyS: continue
            match = True
            for i in range(len(valW)):
                if not (valS[i]==valW[i] or valS[i]>=max(valW[i],3)):
                    match = False
            if match: ans+=1
        return ans
#leetcode submit region end(Prohibit modification and deletion)
