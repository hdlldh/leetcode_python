#Given two words (beginWord and endWord), and a dictionary's word list, find all shortest transformation sequence(s) from beginWord to endWord, such that: 
#
# 
# Only one letter can be changed at a time 
# Each transformed word must exist in the word list. Note that beginWord is not a transformed word. 
# 
#
# Note: 
#
# 
# Return an empty list if there is no such transformation sequence. 
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
#Output:
#[
#  ["hit","hot","dot","dog","cog"],
#  ["hit","hot","lot","log","cog"]
#]
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
#Output: []
#
#Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.
# 
#
# 
# 
# Related Topics Array String Backtracking Breadth-first Search


import collections
#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        wordSet = set(wordList)
        ans = []
        if endWord in wordSet:
            wordSet.remove(endWord)
        else:
            return ans
        if beginWord in wordSet: wordSet.remove(beginWord)
        queue = collections.deque()
        queue.append([beginWord])
        visited = set()
        visited.add(beginWord)
        wordLen = len(beginWord)
        found = False

        while queue and not found:
            visited2 = set()
            for _ in range(len(queue)):
                list1 = queue.popleft();
                word1 = list1[-1]
                for j in range(wordLen):
                    for ch in 'abcdefghijklmnopqrstuvwxyz':
                        if ch == word1[j]: continue
                        word2 = word1[:j] + ch + word1[j + 1:]
                        if word2 == endWord:
                            found = True
                            list2 = list1[:]
                            list2.append(endWord)
                            ans.append(list2)
                        elif word2 in wordSet and word2 not in visited:
                            list2 = list1[:]
                            list2.append(word2)
                            queue.append(list2)
                            visited2.add(word2)
            visited = visited.union(visited2)
        return ans
#leetcode submit region end(Prohibit modification and deletion)
