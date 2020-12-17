# Given a set of words (without duplicates), find all word squares you can build
#  from them. 
# 
#  A sequence of words forms a valid word square if the kth row and column read 
# the exact same string, where 0 ≤ k < max(numRows, numColumns). 
# 
#  For example, the word sequence ["ball","area","lead","lady"] forms a word squ
# are because each word reads the same both horizontally and vertically. 
# 
#  
# b a l l
# a r e a
# l e a d
# l a d y
#  
# 
#  Note: 
#  
#  There are at least 1 and at most 1000 words. 
#  All words will have the exact same length. 
#  Word length is at least 1 and at most 5. 
#  Each word contains only lowercase English alphabet a-z. 
#  
#  
# 
#  Example 1:
#  
# Input:
# ["area","lead","wall","lady","ball"]
# 
# Output:
# [
#   [ "wall",
#     "area",
#     "lead",
#     "lady"
#   ],
#   [ "ball",
#     "area",
#     "lead",
#     "lady"
#   ]
# ]
# 
# Explanation:
# The output consists of two word squares. The order of output does not matter (
# just the order of words in each word square matters).
#  
#  
# 
#  Example 2:
#  
# Input:
# ["abat","baba","atan","atal"]
# 
# Output:
# [
#   [ "baba",
#     "abat",
#     "baba",
#     "atan"
#   ],
#   [ "baba",
#     "abat",
#     "baba",
#     "atal"
#   ]
# ]
# 
# Explanation:
# The output consists of two word squares. The order of output does not matter (
# just the order of words in each word square matters).
#  
#  Related Topics Backtracking Trie


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def wordSquares(self, words):
        """
        :type words: List[str]
        :rtype: List[List[str]]
        """
        n =len(words[0])
        mem = collections.defaultdict(list)
        for word in words:
            for i in range(n):
                mem[word[:i]].append(word)
        mat = [[""]*n for _ in range(n)]
        ans = []
        self.helper(mat, 0, n, mem, ans)
        return ans

    def helper(self, mat, i, n, mem, ans):
        if i == n:
            out = []
            for k in range(n):
                out.append(''.join(mat[k]))
            ans.append(out)
            return
        key = ''.join(mat[i][:i])
        for word in mem[key]:
            mat[i][i] = word[i]
            j = i+1
            while j<n:
                mat[i][j] = word[j]
                mat[j][i] = word[j]
                key = ''.join(mat[j][:i+1])
                if key not in mem: break
                j+= 1
            if j ==n: self.helper(mat, i+1, n, mem, ans)
        
# leetcode submit region end(Prohibit modification and deletion)
