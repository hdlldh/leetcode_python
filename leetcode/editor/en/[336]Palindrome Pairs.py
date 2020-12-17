#Given a list of unique words, find all pairs of distinct indices (i, j) in the given list, so that the concatenation of the two words, i.e. words[i] + words[j] is a palindrome. 
#
# Example 1: 
#
# 
# 
#Input: ["abcd","dcba","lls","s","sssll"]
#Output: [[0,1],[1,0],[3,2],[2,4]] 
#Explanation: The palindromes are ["dcbaabcd","abcddcba","slls","llssssll"]
# 
#
# 
# Example 2: 
#
# 
#Input: ["bat","tab","cat"]
#Output: [[0,1],[1,0]] 
#Explanation: The palindromes are ["battab","tabbat"]
# 
# 
# 
# Related Topics Hash Table String Trie



#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        hmap = {}
        n = len(words)
        ans = []
        for i, word in enumerate(words): hmap[word] = i

        for i in range(n):
            word = words[i]
            m = len(word)
            for j in range(m+1):
                left = word[:j]
                right = word[j:]
                if self.isPalindrome(left):
                    other = right[::-1]
                    if other in hmap and hmap[other]!=i: ans.append([hmap[other], i])
                if self.isPalindrome(right):
                    other = left[::-1]
                    if other in hmap and hmap[other] != i and len(right)!=0: ans.append([i, hmap[other]])
        return ans



    def isPalindrome(self, word):
        n = len(word)
        i = 0
        j = n-1
        while i<j:
            if word[i]!=word[j]: return False
            i+=1
            j-=1
        return True
        
#leetcode submit region end(Prohibit modification and deletion)
