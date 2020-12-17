#Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that: 
#
# 
# Only one letter can be changed at a time. 
# Each transformed word must exist in the word list. Note that beginWord is not a transformed word. 
# 
#
# Note: 
#
# 
# Return 0 if there is no such transformation sequence. 
# All words have the same length. 
# All words contain only lowercase alphabetic characters. 
# You may assume no duplicates in the word list. 
# You may assume beginWord and endWord are non-empty and are not the same. 
# 
#
# Example 1: 
#
# 
#Input:
#beginWord = "hit",
#endWord = "cog",
#wordList = ["hot","dot","dog","lot","log","cog"]
#
#Output: 5
#
#Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
#return its length 5.
# 
#
# Example 2: 
#
# 
#Input:
#beginWord = "hit"
#endWord = "cog"
#wordList = ["hot","dot","dog","lot","log"]
#
#Output: 0
#
#Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.
# 
#
# 
# 
# Related Topics Breadth-first Search


import collections
#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def ladderLength2(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        wordSet = set(wordList)
        if endWord in wordSet: wordSet.remove(endWord)
        else: return 0
        if beginWord in wordSet: wordSet.remove(beginWord)
        wordLen = len(beginWord)
        queue = collections.deque()
        queue.append(beginWord)
        ans = 1
        while queue:
            ans += 1
            for _ in range(len(queue)):
                word1 = queue.popleft()
                for i in range(wordLen):
                    for ch in 'abcdefghijklmnopqrstuvwxyz':
                        if ch == word1[i]: continue
                        word2 = word1[:i] + ch + word1[i + 1:]
                        if word2 == endWord: return ans
                        if word2 in wordSet:
                            queue.append(word2)
                            wordSet.remove(word2)
        return 0

    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        wordSet = set(wordList)
        if endWord not in wordSet: return 0
        wordLen = len(beginWord)
        s1 = set()
        s1.add(beginWord)
        s2 = set()
        s2.add(endWord)
        step = 0
        while s1 and s2:
            step += 1
            if len(s1)>len(s2): s1, s2 = s2, s1
            s = set()
            for word1 in s1:
                for i in range(wordLen):
                    for ch in 'abcdefghijklmnopqrstuvwxyz':
                        if ch == word1[i]: continue
                        word2 = word1[:i] + ch + word1[i + 1:]
                        if word2 in s2: return step + 1
                        if word2 not in wordSet:continue
                        s.add(word2)
                        wordSet.remove(word2)
            s1 = s
        return 0



#leetcode submit region end(Prohibit modification and deletion)
